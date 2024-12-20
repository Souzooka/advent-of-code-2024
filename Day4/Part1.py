import os
import pathlib
from typing import List

# https://adventofcode.com/2024/day/4

# Set current working directory to the one containing this file,
# so opening files also works inside the debugger.
os.chdir(pathlib.Path(__file__).parent.resolve())

# Grab puzzle input lines
lines: List[str] = []
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

search_word = "XMAS"
search_directions = (
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1],
)

# Oof my quad-nested loop
count = 0
# Each potential starting character...
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        # Each potential search direction...
        for search_direction in search_directions:
            # Each character in the search word...
            for k in range(0, len(search_word)):
                # Calculate the indices of the character to check against the search word
                x = i + (search_direction[1] * k)
                y = j + (search_direction[0] * k)
                
                # Indices clamping
                if not 0 <= y < len(lines):
                    break
                if not 0 <= x < len(lines[y]):
                    break

                # Compare the found character against the search word's character
                char = lines[y][x]
                if char != search_word[k]:
                    break

                # If this is the last character, then we found a match
                if k == len(search_word) - 1:
                    count += 1

# Output the result
with open("output1.txt", 'w') as file:
    file.write(str(count))
