import sys
import os
import re
from typing import List

# https://adventofcode.com/2024/day/1

# Set current working directory to the one containing this file,
# so opening files also works inside the debugger.
os.chdir(os.path.dirname(sys.argv[0]))

# Read in lines from string input
lines: List[str] = []
with open("input.txt", 'r') as file:
    lines = file.readlines()

# Create the two columns of numbers, to be sorted later.
lsts: List[List[int]] = [[], []]
for line in lines:
    line = line.strip() # Remove newline
    nums = [int(n) for n in re.split("\s+", line)]
    lsts[0].append(nums[0])
    lsts[1].append(nums[1])

# Now sort each list, ascending
lsts[0].sort()
lsts[1].sort()

# Sum up the absolute differences in each pair of numbers
total = 0
for pair in zip(lsts[0], lsts[1]):
    total += abs(pair[0] - pair[1])

# Output the result
with open("output1.txt", 'w') as file:
    file.write(str(total))
