from collections import Counter
import os
import pathlib
from typing import List, Tuple

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

"""
# In part 2, we'll change the sorting functions to instead
# check how many problem levels exist and, if one of the functions
# detects only one problem, the report may be able to be made safe
# by removing that problem level.
def is_sorted_asc(lst: List[int]) -> Tuple[int, List[int]]:
    num_problems = 0
    problems = []

    for i in range(0, len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            num_problems += 1
            problems.append(i + 1)
    return (num_problems, problems)

def is_sorted_desc(lst: List[int]) -> Tuple[int, List[int]]:
    num_problems = 0
    problems = []

    for i in range(0, len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            num_problems += 1
            problems.append(i)
    return (num_problems, problems)

def is_sorted(lst: List[int]) -> Tuple[int, List[int]]:
    result1 = is_sorted_asc(lst)
    result2 = is_sorted_desc(lst)
    if result1[0] < result2[0]:
        return result1
    return result2

# We can only really make a report "safe" by removing the first
# or last index. We'll make a similar change to check_diff and
# later check if the problem index is the first or last item.
def check_diff(lst: List[int]) -> Tuple[int, List[int]]:
    # Checks that the difference between each number is lte 3,
    # We don't need to check that the difference is at least 1
    # since is_sorted throws out any cases where 2 adjacent numbers
    # are equal.
    num_problems = 0
    problems = []

    for i in range(0, len(lst) - 1):
        if abs(lst[i] - lst[i + 1]) > 3:
            num_problems += 1
            problems.append(i + 1)
    return (num_problems, problems)

def check_report(report, total_problems=0):
    orig_report = list(report)
    num_problems, problems = is_sorted(report)
    total_problems += num_problems
    if num_problems > 1:
        #print(f"is_sorted num problems over 1: {orig_report}, {report}")
        return False
    if num_problems == 1:
        # Splice out the one problem index to try and make report safe
        tmp = list(report)
        del tmp[problems[0]]
        report = tmp
    
    if is_sorted(report)[0] != 0:
        # We still have a problem after removing an item, so this report is unsafe
        #print(f"is_sorted total problems over 1 (pass 2): {orig_report}, {report}")
        return False

    num_problems, problems = check_diff(report)
    total_problems += num_problems
    if total_problems > 1:
        #print(f"total problems over 1: {orig_report}, {report}")
        return False
    if num_problems == 1:
        # If the problem index is the first or last level,
        # we can remove that level to create a report without
        # too significant of differences.
        if 0 < problems[0] < len(report) - 1:
            return False
        tmp = list(report)
        del tmp[problems[0]]
        report = tmp

    if check_diff(report)[0] != 0:
        # We still have a problem after removing an item, so this report is unsafe
        #print(f"check_diff problems over 1 (pass 2): {orig_report}, {report}")
        return False
    
    # The report is safe!
    return True
"""

def check_report(report: List[int]) -> bool:
    if not is_sorted(report):
        # Not gradually increasing or decreasing, unsafe :(
        return False

    if not check_diff(report):
        # Differences between 2 numbers exceed 3, unsafe :(
        return False
    
    # The report is safe!
    return True

# Now tally up the number of safe levels
safe = 0
for report in reports:
    """
    # Before we check the sorting order and differences within the report,
    # We'll check if there are 2 levels with the same number within the report.
    # In that scenario, if the lists from removing either one of those levels is
    # non-compliant, then we cannot make the report safe.
    counts = Counter(report)

    potential_reports = [report]
    found_dupe = 0
    for key, val in counts.items():
        if val > 2:
            found_dupe += val - 1
        if val == 2:
            found_dupe += 1
            if found_dupe > 1:
                break
            report1 = list(report)
            report2 = list(reversed(report))
            del report1[report1.index(key)]
            del report2[report2.index(key)]
            report2.reverse()
            potential_reports = [report1, report2]

    print(found_dupe)
    """
    
    # Brute force because it's 2 AM and I've lost control of my life
    # Will have to figure out what the problem cases were later
    # https://www.youtube.com/watch?v=1vs55Z7t7bk

    for i in range(len(report)):
        if check_report(report[0:i] + report[i+1:len(report)]):
            safe += 1
            break

# Output the result
with open("output1.txt", 'w') as file:
    file.write(str(safe))
