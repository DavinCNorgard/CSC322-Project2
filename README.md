# KenKen SMT Solver
## CSC 322 Project 2
Solving KenKen Puzzle Using an SMT (Integer) Solver

Report link: https://docs.google.com/document/d/1rZLXw-sBfvqEu4YJUPtGHNAP3GBVzrJHME4xNmiT7BE/edit?usp=sharing

## Authors
- Rastin Rashidi [V00963407]
- Davin Norgard [V00929845]
- Jean-Medard Udeh (Jd) [V00940546]
- Radu Ionescu [V00891249]

## Getting Started
### Prerequisites
- Ensure that mathsat is installed.

### Setup the files
To setup the files, simply run the command
```
make
```
This will create a symbolic link for all the Python files which enables you to run kenken2smt, smt2kenken and pp (pretty print) without the .py extention.
For example, you can run 
```
./kenken2smt <puzzle.txt >puzzle.smt
```
Instead of 
```
./kenken2smt.py <puzzle.txt >puzzle.smt
```
## Running the Basic Task
- Ensure that there is a KenKen puzzle contained in a text file. For example, you can have a text file called `puzzle.txt` containing:
```
#kenken www.kenkenpuzzle.com Puzzle 22686 7x7 Hard
r1.240*,r1,r2.72*,r3.6-,r3,r4.2,r5.13+
r6.4-,r1,r2,r7.2-,r8.20*,r8,r5
r6,r1,r2,r7,r8,r8,r9.19+
r10.9+,r10,r11.14*,r11,r12.2/,r9,r9
r10,r13.70*,r11,r14.336*,r12,r9,r9
r15.13+,r13,r13,r14,r16.14+,r16,r16
r15,r15,r15,r14,r14,r17.5-,r17
```
- We have provided a sample one, but you are welcome to change it to a different puzzle!

### Step 1
Generating a `puzzle.smt` file:
```
./kenken2smt (text file containing puzzle) >puzzle.smt
```
For example, if your puzzle is in a text file named `puzzle.txt` you would enter:
```
./kenken2smt puzzle.txt >puzzle.smt
```
This step takes any KenKen puzzle that is in a text file and outputs the SMT constraints into the file `puzzle.smt` for mathsat to solve!

### Step 2
Using mathsat to solve the constraints generated above:
```
mathsat <puzzle.smt >model.smt
```
This takes in the puzzle.smt created by `kenken2smt` and outputs a solved (or unsat) SMT into a file called `model.smt`

### Step 3
Writing the SMT output into `solution.txt` file containing the solved KenKen:
```
./smt2kenken <model.smt >solution.txt
```
This takes in the model.smt created by `mathsat` and outputs the solution of the KenKen puzzle into `solution.txt`

### Step 4
Now that you have the solved KenKen puzzle in `solution.txt`, you can view it in the terminal using `cat` command:
```
cat solution.txt
```

## Running Pretty Print
- There are two steps to running pp (pretty print).

### Step 1
Get the relevent puzzle information from the given website. There is a provided script called fetch that can be used for this given the puzzle id:
```
./fetch.sh <puzzleId> >puzzle.json
```
For example:
```
./fetch.sh 22686 >puzzle.json
```

### Step 2
Now that you have the `puzzle.json` file you can use pp (pretty print). You can print out the `puzzle.json` to the console with the following command:
```
./pp puzzle.json
```
Or alternatively, the puzzle can be printed in a text file using the following command:
 ```
./pp puzzle.json >ppPuzzle.txt
```
