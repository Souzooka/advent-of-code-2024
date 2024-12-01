from collections import Counter
import sys
import os
import re
from typing import List

# https://adventofcode.com/2024/day/1#part2

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

# Now to calculate similarity score, we'll need to know the number
# of occurrences for each number in the right column.
# There's a good class for doing this quickly, collections.Counter.
# We can actually more quickly calculate the similarity score if we
# convert the left column to a Counter as well.
# For example, in the example, there are 3 3's in the left column, and
# 3 in the right. This sums into a similarity score of
# (3 * 3) + (3 * 3) + (3 * 3), but that is also the same as 3 * 3 * 3

# Convert each list into a Counter
lcount = Counter(lsts[0])
rcount = Counter(lsts[1])

# Calculate similarity score by multiplying the left number
# by the amount of times the right number appears,
# by the amount of times the left number appears
total = 0
for l, ln in lcount.items():
    rn = rcount.get(l, 0)
    total += (l * rn * ln)

# Output the result
with open("output2.txt", 'w') as file:
    file.write(str(total))
