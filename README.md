# KenKen SMT Solver
## CSC 322 Project 2
Solving KenKen Puzzle Using an SMT (Integer) Solver

Report link: https://docs.google.com/document/d/1rZLXw-sBfvqEu4YJUPtGHNAP3GBVzrJHME4xNmiT7BE/edit?usp=sharing

## Authors
- Rastin Rashidi [V00963407]
- Davin Norgard [V00929845]
- Jean-Medard Udeh (Jd) [V00940546]
- 

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
- Ensure that there is a KenKen puzzle in a file called `puzzle.txt`
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
Using matsat to solve the constraints generated above:
```
mathsat <puzzle.smt >model.smt
```
This takes in the puzzle.smt created by `kenken2smt` and outputs a solved (or unsat) SMT.

### Step 3
Writing the SMT output into `solution.txt` file containing the solved KenKen:
```
./smt2kenken <model.smt >solutions.txt
```
This takes in the model.smt created by `mathsat` and outputs the solution to the KenKen puzzle into `solutions.txt`

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
