# KenKen SMT Solver
## CSC 322 Project 2
Solving KenKen Puzzle Using an SMT (Integer) Solver

## Authors
- Rastin Rashidi [V00963407]
- 
- 
- 

## Getting Started
### Prerequisites
- Ensure that mathsat is installed.

### Setup the files
To setup the files, simply run the command
```
make
```
This will create a symbolic link for all the Python files.
## Running the Basic Task
- Ensure that there is a KenKen puzzle in a file called `puzzle.txt`
- We have provided a sample one, but you are welcome to change it to a different puzzle!

### Step 1
Generating a `puzzle.smt` file:
```
./kenken2smt <puzzle.txt >puzzle.smt
```

### Step 2
Using matsat to solve the constraints generated above:
```
mathsat <puzzle.smt >model.smt
```

### Step 3
Writing the SMT output into `solution.txt` file containing the solved KenKen:
```
./smt2kenken <model.smt >solutions.txt
```

### Step 4
Now that you have the solved KenKen puzzle in `solution.txt`, you can view it in the terminal using `cat` command:
```
cat solution.txt
```
