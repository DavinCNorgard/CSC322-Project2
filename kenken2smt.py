f = open("puzzle.smt", 'w')
f.write("(set-logic UFNIA)\n(set-option :produce-models true)\n(set-option :produce-assignments true)\n")
for i in range(49):
    f.write("(declare-const V"+str(i)+" Int)\n")
for i in range(49):
    f.write("(assert (and (> V"+str(i)+" 0) (< V"+str(i)+" 10)))\n")
for i in range(7):
    if i > 0:
        i = i * 7
    f.write("(assert (distinct V"+str(i)+" V"+str(i+1)+" V"+str(i+2)+" V"+str(i+3)+" V"+str(i+4)+" V"+str(i+5)+" V"+str(i+6)+" ))\n")
for i in range(7):
    f.write("(assert (distinct V"+str(i)+" V"+str(i+7)+" V"+str(i+14)+" V"+str(i+21)+" V"+str(i+28)+" V"+str(i+35)+" V"+str(i+42)+" ))\n")

## add the constraints here
constraints = []
count = 0

if len(sys.argv) != 2:
    print("Invalid syntax. Use ./kenken2smt <puzzle file>\n")
with open(sys.argv[1], 'r') as fInput:
    for line in fInput:
        if '#' in line:
            continue
        char = line.split(",")
        for i in char:
            i = i.split(".")
            i.append("V"+str(count))
            constraints.append(i)
            count = count + 1
print(constraints)
##

f.write("(check-sat)\n")
f.write("(get-value (")
for i in range(49):
    f.write("V"+str(i)+" ")
f.write("))\n")
f.write("(exit)\n")
