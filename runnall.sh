bash
Copy code
#!/bin/bash

# Set the folder path
folder_path="/Users/raduionescu/Documents/csc322/CSC322-Project2/7/a/easy" 

# Set the command to run on each file
command_to_run="echo"

# Loop through all the files in the folder and run the command on each one
for file_path in "$folder_path"/*
do
    "python3 ./kenken2smt <puzzle.smt>" "$file_path"
    
done