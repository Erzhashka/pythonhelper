"""Main maze generator and visualizer program."""

import sys
import random
from typing import List, Tuple, Optional
from collections import deque
from config import load_config
from visualizer import MazeVisualizer


def find_shortest_path(
    maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]
) -> Optional[str]:
    """Find the shortest path from start to end using BFS.

    Args:
        maze: 2D list of hex values representing maze cells.
        start: Tuple (x, y) for start position.
        end: Tuple (x, y) for end position.

    Returns:
        String of N/E/S/W moves or None if no path exists.
    """
    if start == end:
        return ""

    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    # Direction mappings: (dx, dy, wall_bit, opposite_wall_bit, letter)
    directions = [
        (0, -1, 0, 2, "N"),  # North
        (1, 0, 1, 3, "E"),  # East
        (0, 1, 2, 0, "S"),  # South
        (-1, 0, 3, 1, "W"),  # West
    ]

    visited: set = {start}
    queue: deque = deque([(start, "")])
    result: str = ""

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            result = path
            break

        cell = maze[y][x]

        for dx, dy, wall_bit, opp_wall_bit, letter in directions:
            nx, ny = x + dx, y + dy

            # Check bounds
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                # Check if wall is open (bit = 0)
                if not ((cell >> wall_bit) & 1):
                    neighbor = maze[ny][nx]
                    # Verify opposite wall is also open
                    if not ((neighbor >> opp_wall_bit) & 1):
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + letter))

    return result if result else None


def embed_pattern_42(maze: List[List[int]]) -> bool:
    """Embed the "42" pattern as fully closed cells in the maze.

    The pattern is placed roughly in the center of the maze.

    Args:
        maze: 2D list of hex values representing maze cells.

    Returns:
        True if pattern was embedded, False if maze too small.
    """
    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    # Pattern "42" requires minimum 10x5 area for visibility
    if width < 10 or height < 5:
        return False

    # Position pattern in center
    start_x = (width - 8) // 2
    start_y = (height - 4) // 2

    # Ensure position is valid
    if start_x < 1 or start_y < 1 or start_x + 8 >= width or start_y + 4 >= height:
        return False

    # "4" pattern (roughly)
    pattern_4 = [
        (0, 0), (2, 0),
        (0, 1), (1, 1), (2, 1),
        (2, 2),
        (2, 3),
    ]

    # "2" pattern
    pattern_2 = [
        (4, 0), (5, 0), (6, 0),
        (6, 1),
        (4, 2), (5, 2), (6, 2),
        (4, 3), (5, 3), (6, 3),
    ]

    # Close cells and update all neighbors' walls
    for dx, dy in pattern_4 + pattern_2:
        x, y = start_x + dx, start_y + dy
        if 0 <= x < width and 0 <= y < height:
            maze[y][x] = 15  # All walls = 1111

            # Update all neighbors to have walls facing this closed cell
            if y > 0:  # North neighbor
                maze[y - 1][x] |= 4  # Set south wall
            if y < height - 1:  # South neighbor
                maze[y + 1][x] |= 1  # Set north wall
            if x > 0:  # West neighbor
                maze[y][x - 1] |= 2  # Set east wall
            if x < width - 1:  # East neighbor
                maze[y][x + 1] |= 8  # Set west wall

    return True


def constrain_corridor_width(maze: List[List[int]]) -> None:
    """Constrain corridor width to maximum 2 cells.

    Iteratively fills cells to prevent 3x3 open areas.

    Args:
        maze: 2D list of hex values (modified in place).
    """
    height = len(maze)
    width = len(maze[0]) if height > 0 else 0

    # Check for 3x3 completely open areas and constrain them
    changed = True
    iterations = 0
    max_iterations = 100

    while changed and iterations < max_iterations:
        changed = False
        iterations += 1

        for y in range(height - 2):
            for x in range(width - 2):
                # Check for 3x3 completely open area
                open_count = 0

                for dy in range(3):
                    for dx in range(3):
                        if maze[y + dy][x + dx] == 0:  # Completely open cell
                            open_count += 1

                # If 3x3 has all 9 cells open, close the center one
                if open_count == 9:
                    cy, cx = y + 1, x + 1
                    maze[cy][cx] = 15  # Close center cell completely

                    # Update neighboring cells' walls to match
                    if cy > 0:  # Update north neighbor
                        maze[cy - 1][cx] |= 4  # Set south wall on north neighbor
                    if cy < height - 1:  # Update south neighbor
                        maze[cy + 1][cx] |= 1  # Set north wall on south neighbor
                    if cx > 0:  # Update west neighbor
                        maze[cy][cx - 1] |= 2  # Set east wall on west neighbor
                    if cx < width - 1:  # Update east neighbor
                        maze[cy][cx + 1] |= 8  # Set west wall on east neighbor

                    changed = True


def create_maze(
    width: int, height: int, seed: int, perfect: bool = False
) -> List[List[int]]:
    """Generate a maze using Depth-First Search.

    Args:
        width: Maze width in cells.
        height: Maze height in cells.
        seed: Random seed for reproducibility.
        perfect: If True, ensure single path between entry and exit.

    Returns:
        2D list of hex values representing maze cells.
    """
    random.seed(seed)

    # Initialize all cells with all walls (15 = 0b1111)
    maze = [[15 for _ in range(width)] for _ in range(height)]

    def carve(x: int, y: int) -> None:
        """Carve passages using recursive backtracking.

        Args:
            x: X coordinate.
            y: Y coordinate.
        """
        # Mark cell as visited by removing all its walls initially
        maze[y][x] = 0

        # Directions: (dx, dy, wall_bit, opposite_bit)
        # wall_bit: which wall to remove from current cell
        # opposite_bit: which wall to remove from neighbor
        directions = [(0, -1, 0, 2), (1, 0, 1, 3), (0, 1, 2, 0), (-1, 0, 3, 1)]
        random.shuffle(directions)

        for dx, dy, wall_bit, opp_bit in directions:
            nx, ny = x + dx, y + dy

            # If neighbor is in bounds and not visited (still has all walls = 15)
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 15:
                # Remove wall between current cell and neighbor
                maze[y][x] &= ~(1 << wall_bit)
                maze[ny][nx] &= ~(1 << opp_bit)

                # Recursively carve from neighbor
                carve(nx, ny)

    # Carve passages from (0, 0)
    carve(0, 0)

    # Add external walls back for border cells
    for y in range(height):
        for x in range(width):
            if y == 0:
                maze[y][x] |= 1  # North wall
            if y == height - 1:
                maze[y][x] |= 4  # South wall
            if x == 0:
                maze[y][x] |= 8  # West wall
            if x == width - 1:
                maze[y][x] |= 2  # East wall

    # Create openings at entry and exit
    maze[0][0] &= ~1  # Remove north wall at (0, 0)
    maze[height - 1][width - 1] &= ~4  # Remove south wall at exit

    # Embed the "42" pattern
    if not embed_pattern_42(maze):
        print("Note: Maze too small for '42' pattern", file=sys.stderr)

    # Constrain corridor widths
    constrain_corridor_width(maze)

    return maze


def write_maze_to_file(
    maze: List[List[int]],
    filepath: str,
    entry: Tuple[int, int],
    exit_pos: Tuple[int, int],
    solution_path: Optional[str] = None,
) -> None:
    """Write maze to file in required format.

    Args:
        maze: 2D list of hex values.
        filepath: Output file path.
        entry: Entry coordinates.
        exit_pos: Exit coordinates.
        solution_path: Solution path as string or None.
    """
    try:
        with open(filepath, "w") as f:
            # Write maze grid
            for row in maze:
                line = "".join(format(cell, "x") for cell in row)
                f.write(line + "\n")

            # Empty line
            f.write("\n")

            # Write metadata
            f.write(f"{entry[0]},{entry[1]}\n")
            f.write(f"{exit_pos[0]},{exit_pos[1]}\n")

            if solution_path:
                f.write(solution_path + "\n")
            else:
                f.write("\n")

    except IOError as e:
        print(f"Error writing to file: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Main program entry point."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config.txt>", file=sys.stderr)
        sys.exit(1)

    config_file = sys.argv[1]

    try:
        config = load_config(config_file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.",
              file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading configuration: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate required config keys
    required_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE",
                     "PERFECT"]
    for key in required_keys:
        if key not in config:
            print(f"Error: Missing required config key '{key}'.",
                  file=sys.stderr)
            sys.exit(1)

    # Parse configuration
    try:
        width: int = config["WIDTH"]
        height: int = config["HEIGHT"]
        entry_str: str = config["ENTRY"]
        exit_str: str = config["EXIT"]
        entry_parts = entry_str.split(",")
        exit_parts = exit_str.split(",")
        entry = (int(entry_parts[0]), int(entry_parts[1]))
        exit_pos = (int(exit_parts[0]), int(exit_parts[1]))
        output_file: str = config["OUTPUT_FILE"]
        perfect: bool = config["PERFECT"]
        # Use provided seed or random for different mazes each time
        seed: int = config.get("SEED", random.randint(0, 2**31 - 1))

        # Validate coordinates
        if not (0 <= entry[0] < width and 0 <= entry[1] < height):
            raise ValueError(f"Entry coordinates {entry} out of bounds")
        if not (0 <= exit_pos[0] < width and 0 <= exit_pos[1] < height):
            raise ValueError(f"Exit coordinates {exit_pos} out of bounds")
        if entry == exit_pos:
            raise ValueError("Entry and exit must be different")

    except (ValueError, IndexError) as e:
        print(f"Error parsing configuration: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate maze
    print(f"Generating maze {width}x{height}...", file=sys.stderr)
    maze = create_maze(width, height, seed, perfect)

    # Find shortest path
    print("Finding shortest path...", file=sys.stderr)
    solution_path = find_shortest_path(maze, entry, exit_pos)

    if not solution_path:
        print("Error: No path found from entry to exit.", file=sys.stderr)
        sys.exit(1)

    # Write to file
    print(f"Writing maze to {output_file}...", file=sys.stderr)
    write_maze_to_file(maze, output_file, entry, exit_pos, solution_path)

    # Display visualizer
    print("Launching visualizer...", file=sys.stderr)
    visualizer = MazeVisualizer(maze, entry, exit_pos, solution_path)
    visualizer.display()


if __name__ == "__main__":
    main()
