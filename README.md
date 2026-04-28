# A-Maze-ing: Terminal Maze Generator & Visualizer

*This project has been created as part of the 42 curriculum by etoktona.*

## Description

**A-Maze-ing** is a Python-based maze generator and terminal visualizer. The project generates random mazes using the Depth-First Search (DFS) algorithm, enforces corridor width constraints, embeds a "42" pattern, exports them in hexadecimal format, finds the shortest solution path, and provides an interactive terminal-based visualization with real-time controls.

### Key Features

- **Procedural Maze Generation**: Creates unique mazes with configurable dimensions
- **Corridor Width Constraint**: Ensures no 3x3 open areas (corridors max 2 cells wide)
- **"42" Pattern Embedding**: Visible as fully closed cells (█) in the maze
- **Terminal Visualization**: ASCII art rendering with box-drawing characters
- **Path Finding**: Automatic BFS-based solution path calculation
- **Interactive Controls**: Toggle path display, change wall colors
- **Reproducible Output**: Seed-based generation for consistent maze creation
- **Hexadecimal Encoding**: Standard wall representation format
- **Reusable Module**: Exportable maze generation logic

## Installation

### Prerequisites

- Python 3.10 or later
- pip package manager

### Quick Start

```bash
# Install dependencies
make install

# Run the maze generator
make run

# Run with debug mode
make debug

# Clean generated files and caches
make clean
```

## Usage

### Basic Command

```bash
python3 a_maze_ing.py config.txt
```

This will:
1. Load configuration from `config.txt`
2. Generate a maze according to specifications
3. Apply corridor width constraints
4. Embed the "42" pattern
5. Find the shortest path from entry to exit
6. Write the maze to the output file
7. Launch the interactive terminal visualizer

### Configuration File Format

The `config.txt` file uses `KEY=VALUE` pairs (one per line). Lines starting with `#` are comments.

**Required Keys:**

| Key | Description | Example |
|-----|-------------|---------|
| `WIDTH` | Maze width in cells | `WIDTH=20` |
| `HEIGHT` | Maze height in cells | `HEIGHT=15` |
| `ENTRY` | Entry coordinates (x,y) | `ENTRY=0,0` |
| `EXIT` | Exit coordinates (x,y) | `EXIT=19,14` |
| `OUTPUT_FILE` | Output filename | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Perfect maze (single path) | `PERFECT=False` |
| `SEED` | Random seed (optional) | `SEED=42` |

### Example Configuration

```
# Maze Configuration
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=False
# SEED=42          # Uncomment to reproduce specific maze
```

**Note**: If `SEED` is commented out or omitted, a random seed is used each time, generating **different mazes** on every run.

## Terminal Visualizer Controls

When the visualizer launches, you can interact with the maze using these controls:

- **[p]** - Toggle solution path display (show/hide the dots)
- **[c]** - Change wall colors (select from 7 color options)
- **[q]** - Quit the visualizer

### Color Options

1. **Cyan** (default)
2. **Yellow**
3. **Green**
4. **Red**
5. **Magenta**
6. **White**
7. **Blue**

### Visualization Symbols

- **S** = Start/Entry (green)
- **E** = Exit (red)
- **·** = Solution path (yellow/gold)
- **█** = Pattern "42" - fully closed cells (magenta)
- **│** = Vertical wall
- **─** = Horizontal wall
- **┼** = Wall junction

## Maze Features

### Corridor Width Constraint

The maze enforces a maximum corridor width of 2 cells. This means:
- ✅ 2x2 open areas are allowed
- ✅ 2x3 open areas are allowed
- ❌ 3x3 open areas are NOT allowed

If the generation creates any 3x3 open area, the algorithm automatically closes the center cell.

### Pattern "42" Embedding

The pattern "42" is embedded as fully closed cells (value = 15, all walls = 1111):

```
4  4
###
4
4

###
  4
 4
###
```

- Displayed with the **█** (solid block) character in magenta
- Positioned roughly in the center of the maze
- Only embedded if the maze is large enough (minimum 10×5)
- If maze is too small, a message is printed to stderr

## Output File Format

The maze is saved to a file specified in the configuration with the following structure:

### Hexadecimal Encoding

Each cell is represented by one hexadecimal digit encoding its walls:

| Bit | Value | Direction | Meaning |
|-----|-------|-----------|---------|
| 0 | 1 | North | North wall |
| 1 | 2 | East | East wall |
| 2 | 4 | South | South wall |
| 3 | 8 | West | West wall |

- Bit = 1: Wall is closed (present)
- Bit = 0: Wall is open (passage)

**Examples:**
- `0x0` (0000): All walls open - completely open cell
- `0xF` (1111): All walls closed - fully blocked cell (pattern "42")
- `0x3` (0011): North and East walls closed, South and West open
- `0xA` (1010): East and West walls closed, North and South open

### File Structure

```
<hex grid - one row per line>

<empty line>
<entry coordinates>
<exit coordinates>
<solution path as N/E/S/W moves>
```

**Example:**

```
f83f3f3f3f3f3f3
f80000000000032
f80808080808032
f80000000000032
f83f3f3f3f3f3f3

0,0
4,2
EESSSENESE
```

## Maze Generation Algorithm

### Algorithm: Recursive Backtracking (Depth-First Search)

**Why this algorithm?**

- Creates perfect mazes with exactly one path between any two points
- O(width × height) optimal complexity
- Natural randomness produces varied maze patterns
- Fast enough for interactive terminal use
- Industry standard for procedural generation

### Generation Steps:

1. Initialize all cells with all walls (value = 15)
2. Start from entrance cell (0, 0)
3. Mark current cell as visited (set value = 0)
4. Randomly choose an unvisited neighbor
5. Remove wall between current and neighbor
6. Recursively carve from the neighbor
7. When no unvisited neighbors remain, backtrack
8. Restore exterior walls for maze boundaries
9. Create openings at entry and exit points
10. Embed the "42" pattern
11. Constrain corridor widths (remove 3x3 open areas)

## Validation

The project includes a **validation tool** that checks maze integrity:

```bash
python3 output_validator.py maze.txt
```

This verifies:
- ✓ Wall consistency between neighboring cells
- ✓ Correct hexadecimal encoding
- ✓ Valid maze structure

## Code Quality

### Testing

```bash
# Run all linters
make lint

# Run strict type checking
make lint-strict
```

Checks performed:
- **flake8**: Code style enforcement (PEP 8)
- **mypy**: Static type checking with strict mode

### Type Safety

- ✓ Full type hints on all functions
- ✓ All functions pass mypy without errors
- ✓ Proper resource management
- ✓ Exception handling throughout
- ✓ Comprehensive docstrings (PEP 257)

## File Structure

```
mazing/
├── a_maze_ing.py           # Main program (generation + path-finding)
├── visualizer.py           # Terminal visualization
├── config.py               # Configuration file loader
├── output_validator.py     # Maze validation tool
├── config.txt              # Default configuration
├── maze.txt                # Generated maze output
├── Makefile                # Build automation
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Examples

### Basic Maze Generation

```bash
$ python3 a_maze_ing.py config.txt
Generating maze 20x15...
Finding shortest path...
Writing maze to maze.txt...
Launching visualizer...
```

### Different Maze Each Time

The default `config.txt` has `SEED` commented out, so each run generates a different maze:

```bash
$ python3 a_maze_ing.py config.txt  # Maze 1 (random seed)
$ python3 a_maze_ing.py config.txt  # Maze 2 (different random seed)
$ python3 a_maze_ing.py config.txt  # Maze 3 (another random seed)
```

### Reproducible Maze

Uncomment `SEED=42` to generate the same maze every time:

```bash
$ echo "SEED=42" >> config.txt
$ python3 a_maze_ing.py config.txt  # Maze A
$ python3 a_maze_ing.py config.txt  # Same Maze A
```

### Validation

```bash
$ python3 output_validator.py maze.txt
✓ Maze is valid (15x20)
```

## Requirements Met

### Mandatory Features

- ✅ Configuration file support (WIDTH, HEIGHT, ENTRY, EXIT, OUTPUT_FILE, PERFECT)
- ✅ Maze generation with reproducible seeds
- ✅ Hexadecimal wall encoding
- ✅ Solution path finding (BFS)
- ✅ Terminal ASCII visualization
- ✅ Interactive user controls
- ✅ Path display toggle
- ✅ Wall color customization
- ✅ Error handling and validation
- ✅ Type hints and mypy compliance
- ✅ Proper resource management
- ✅ Comprehensive docstrings (Google style)
- ✅ Makefile with required targets
- ✅ **Corridor width constraint (max 2 cells)**
- ✅ **"42" pattern embedding**

### Extra Features

- Multiple color themes
- Box-drawing characters for professional appearance
- Validation tool for maze integrity
- Makefile automation
- Comprehensive README with examples

## Notes

- Generated mazes are guaranteed to be solvable
- The "42" pattern is embedded for mazes 10×5 or larger
- Corridors are automatically constrained to maximum 2-cell width
- Terminal must support ANSI color codes for full visualization
- Seed value ensures reproducible maze generation for testing

---

**Version**: 1.0  
**Python Version**: 3.10+  
**Status**: ✅ Complete and Fully Functional
