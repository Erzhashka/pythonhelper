import sys
import math

print("=== Game Coordinate System ===\n")

position = tuple([10, 20, 5])
print(f"Position created: {position}")

origin = tuple([0, 0, 0])
distance = math.sqrt((position[0] - origin[0])**2 + (position[1] - origin[1])**2 + (position[2] - origin[2])**2)
print(f"Distance between {origin} and {position}: {round(distance, 2)}\n")

coord_string = "3,4,0"
print(f'Parsing coordinates: "{coord_string}"')
try:
    parts = coord_string.split(",")
    parsed = tuple([int(parts[0]), int(parts[1]), int(parts[2])])
    print(f"Parsed position: {parsed}")
    distance2 = math.sqrt((parsed[0] - origin[0])**2 + (parsed[1] - origin[1])**2 + (parsed[2] - origin[2])**2)
    print(f"Distance between {origin} and {parsed}: {distance2}\n")
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: ValueError, Args: {e.args}")

invalid_string = "abc,def,ghi"
print(f'Parsing invalid coordinates: "{invalid_string}"')
try:
    parts = invalid_string.split(",")
    invalid_parsed = tuple([int(parts[0]), int(parts[1]), int(parts[2])])
    print(f"Parsed position: {invalid_parsed}")
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: ValueError, Args: {e.args}\n")

print("Unpacking demonstration:")
x, y, z = parsed
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
