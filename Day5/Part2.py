import os
import pathlib
from typing import List, Tuple

# https://adventofcode.com/2024/day/5

# Set current working directory to the one containing this file,
# so opening files also works inside the debugger.
os.chdir(pathlib.Path(__file__).parent.resolve())

# Grab puzzle input rules/updates
rules: List[Tuple[int, int]] = []
updates: List[List[int]] = []
with open("input.txt", "r") as file:
    # The input consists of two parts -- lines for rules, and lines for updates
    # An empty line delineates the two parts.

    # Read in rules until we encounter the empty line (it'll contain a newline in this case)
    while (line := file.readline()) != '\n':
        rules.append(tuple(int(x) for x in line.split('|')))
    
    # Read in updates (EOF will give us a zero-length line)
    while len(line := file.readline()) != 0:
        updates.append([int(x) for x in line.split(',')])

# Updates which were originally broken, made to conform to the rules
corrected_updates: List[List[int]] = []

for update in updates:
    valid = True
    clean = False # We'll need to do multiple passes to make sure all rules apply after making swaps
    update = update.copy() # Just to avoid input mutation

    # Hope none of the rules conflict with eachother and cause infinite loops :)
    while not clean:
        clean = True
        for rule in rules:
            # Find the indicies of both pages listed in the rule within the update
            index1 = -1
            index2 = -1
            for i, v in enumerate(update):
                if rule[0] == v:
                    index1 = i
                if rule[1] == v:
                    index2 = i
            
            # If we haven't found both indices, this rule is not applicable
            if index1 == -1 or index2 == -1:
                continue

            # If the first page in the rule occurs in the update after the second page in the rule,
            # this update is invalid.
            if index1 > index2:
                # Correct the update by swapping the two pages
                # Everyone knows the most efficient means of swapping two variables is tuple unpacking
                update[index1], update[index2] = update[index2], update[index1]
                valid = False
                # This update failed to meet all rules on this pass, so it'll have to go through
                # at least one more pass to make sure it conforms.
                clean = False
    
    # If we found a rulebreak, keep this update
    if not valid:
        corrected_updates.append(update)

# Now that we have all the corrected updates, we can just sum up the middle page of each to get
# our solution.
total = 0
for update in corrected_updates:
    assert(len(update) % 2 == 1)
    total += update[len(update) // 2]

# Output the result
with open("output2.txt", 'w') as file:
    file.write(str(total))
