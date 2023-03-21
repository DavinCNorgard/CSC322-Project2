#!/usr/bin/env python3
import sys
import re
from itertools import permutations

# Declare variables used
constraints = []
count = 0

# Open input file and store information
if len(sys.argv) != 1:
    print("Invalid syntax. Use ./kenken2smt <puzzle file>")
    exit()
with open('puzzle.txt', 'r') as fInput:
    for line in fInput:
        if '#' in line:
            continue
        char = line.split(",")
        for i in char:
            i = re.sub('\n', '', i)
            i = i.split(".")
            i.append("V"+str(count))
            constraints.append(i)
            count = count + 1

# Create output file and write information
f = open("puzzle.smt", 'w')
f.write("(set-logic UFNIA)\n(set-option :produce-models true)\n(set-option :produce-assignments true)\n")
for i in range(49):
    f.write("(declare-const V"+str(i)+" Int)\n")
for i in range(49):
    f.write("(assert (and (> V"+str(i)+" 0) (< V"+str(i)+" 8)))\n")

# Add single box numbers if given any
for i in range(len(constraints)):
    if len(constraints[i])==3:
        cur = constraints[i][0]
        operator = ''
        if '+' in constraints[i][1]:
            operator = '+'
        if '*' in constraints[i][1]:
            operator = '*'
        if '/' in constraints[i][1]:
            operator = '/'
        if '-' in constraints[i][1]:
            operator = '-'
        if operator == '':
            f.write("(assert (= "+constraints[i][2]+" "+constraints[i][1]+"))\n")
            continue

# Ensure all rows and columns have distinct numbers
for i in range(7):
    if i > 0:
        i = i * 7
    f.write("(assert (distinct V"+str(i)+" V"+str(i+1)+" V"+str(i+2)+" V"+str(i+3)+" V"+str(i+4)+" V"+str(i+5)+" V"+str(i+6)+" ))\n")
for i in range(7):
    f.write("(assert (distinct V"+str(i)+" V"+str(i+7)+" V"+str(i+14)+" V"+str(i+21)+" V"+str(i+28)+" V"+str(i+35)+" V"+str(i+42)+" ))\n")

# Add constraints (addition/multiplication) to the output file
for i in range(len(constraints)):
    if len(constraints[i])==3:
        cur = constraints[i][0]
        operator = ''
        if '+' in constraints[i][1]:
            operator = '+'
            result = constraints[i][1].strip('+')
        if '*' in constraints[i][1]:
            operator = '*'
            result = constraints[i][1].strip('*')
        if '/' in constraints[i][1]:
            result = constraints[i][1].strip('/')
            operator = '/'
            regions = []
            regions.append(constraints[i][2])
            for j in range(len(constraints)):
                if cur == constraints[j][0] and len(constraints[j])==2:
                    regions.append(constraints[j][1])
            combo = list(permutations(regions, len(regions)))
            f.write("(assert (or ")
            for i in range(len(combo)):
                f.write(" (= "+result+" ("+operator)
                for j in range(len(combo)):
                    f.write(" "+combo[i][j])
                f.write("))")
            f.write("))\n")
            continue
        if '-' in constraints[i][1]:
            result = constraints[i][1].strip('-')
            operator = '-'
            regions = []
            regions.append(constraints[i][2])
            for j in range(len(constraints)):
                if cur == constraints[j][0] and len(constraints[j])==2:
                    regions.append(constraints[j][1])
            combo = list(permutations(regions, len(regions)))
            f.write("(assert (or ")
            for i in range(len(combo)):
                f.write(" (= "+result+" ("+operator)
                for j in range(len(combo)):
                    f.write(" "+combo[i][j])
                f.write("))")
            f.write("))\n")
            continue
        if operator == '':
            continue
        f.write("(assert (= "+result+" ("+operator+" "+constraints[i][2])
        for j in range(len(constraints)):
            if cur == constraints[j][0] and len(constraints[j])==2:
                f.write(" "+constraints[j][1])
        f.write('))) \n')

# Add output file final lines
f.write("(check-sat)\n")
f.write("(get-value (")
for i in range(49):
    f.write("V"+str(i)+" ")
f.write("))\n")
f.write("(exit)\n")
