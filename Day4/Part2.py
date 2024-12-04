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

# The characters in the X-MAS cross
search_word = "MMASS"

# Starting from one of the M, search in 4 out of the 8 possible directions.
# Each of the crosses can be found from 2 directions, so only checking non-opposing
# directions is more efficient and avoids duplicates
#
#   *.S | S.* | S.S | *.M
#   .A. | .A. | .A. | .A.
#   M.S | S.M | *.M | S.S
search_offsets = (
    [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    [(0, 0), (0, 2), (-1, 1), (-2, 0), (-2, 2)],
    [(0, 0), (2, 0), (1, -1), (0, -2), (2, -2)],
    [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)],
)

# Oof my quad-nested loop
count = 0
# Each potential starting character...
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        # Each potential search direction...
        for search_offset in search_offsets:
            # Each character in the search word...
            for c in range(0, len(search_word)):
                # Calculate the indices of the character to check against the search word
                x = j + search_offset[c][0]
                y = i + search_offset[c][1]

                # Indices clamping
                if not 0 <= y < len(lines):
                    break
                if not 0 <= x < len(lines[y]):
                    break

                # Compare the found character against the search word's character
                char = lines[y][x]
                if char != search_word[c]:
                    break

                # If this is the last character, then we found a match
                if c == len(search_word) - 1:
                    count += 1

# Output the result
with open("output2.txt", 'w') as file:
    file.write(str(count))
