import os
import pathlib
from typing import List

# https://adventofcode.com/2024/day/2

# Set current working directory to the one containing this file,
# so opening files also works inside the debugger.
os.chdir(pathlib.Path(__file__).parent.resolve())

# Read in lines from string input as our reports
# and convert the into a collection of integer levels
reports: List[List[int]] = []
with open("input.txt", 'r') as file:
    for report in file.readlines():
        report = report.strip() # Remove newline
        reports.append([int(n) for n in report.split()])

# Some helper functions to determine if our reports are sorted
# ascending or descending (we don't care which, later on)
# NOTE: If two adjacent elements are equal, the list is also
# not considered "sorted," in this problem space.
def is_sorted_asc(lst: List[int]) -> bool:
    for i in range(0, len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

def is_sorted_desc(lst: List[int]) -> bool:
    for i in range(0, len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            return False
    return True

def is_sorted(lst: List[int]) -> bool:
    return is_sorted_asc(lst) or is_sorted_desc(lst)

def check_diff(lst: List[int]) -> bool:
    # Checks that the difference between each number is lte 3,
    # We don't need to check that the difference is at least 1
    # since is_sorted throws out any cases where 2 adjacent numbers
    # are equal.
    for i in range(0, len(lst) - 1):
        if abs(lst[i] - lst[i + 1]) > 3:
            return False
    return True

# Now tally up the number of safe levels
safe = 0
for report in reports:
    if not is_sorted(report):
        # Not gradually increasing or decreasing, unsafe :(
        continue

    if not check_diff(report):
        # Differences between 2 numbers exceed 3, unsafe :(
        continue
    
    # The report is safe!
    safe += 1

# Output the result
with open("output1.txt", 'w') as file:
    file.write(str(safe))
