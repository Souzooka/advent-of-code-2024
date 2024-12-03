import os
import pathlib
import re
from typing import List, Tuple

# https://adventofcode.com/2024/day/3

# Set current working directory to the one containing this file,
# so opening files also works inside the debugger.
os.chdir(pathlib.Path(__file__).parent.resolve())

# Grab puzzle input as one big line
text = ""
with open("input.txt", "r") as file:
    text = "".join(file.readlines())

# Extract the numbers out of correctly-formed mul operations and convert to int
pattern = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
matches = re.findall(pattern, text)
operands: List[Tuple[int, int]] = [tuple(int(x) for x in pair) for pair in matches]

# Sum up the multiplications
sum = 0
for l, r in operands:
    sum += l * r

# Output the result
with open("output1.txt", 'w') as file:
    file.write(str(sum))
