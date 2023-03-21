#!/usr/bin/env python3
import sys
import re

# Declare variables
given = []
result = []

# Open solved SMT file and store the information in the given list
with open('model.smt', 'r') as f:
    for line in f:
        line = re.sub('\n', '', line)
        given.append(line.split(")"))
        if "unsat" in line:
            print("Puzzle is not satisfiable.")
            exit()

# Add the results given to the results list
for i in range(1, 50):
    cur = given[i][0] 
    cur = cur.split(" ")
    if i == 1:
        result.append(cur[2])
    else:
        result.append(cur[3])

# Create new solutions file and write solutions
solution = open('solutions.txt', 'w')
for i in range(49):
    solution.write(result[i])
solution.write("\n")
