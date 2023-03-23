#!/usr/bin/env python3
import sys
import json

#format the string matrix into a 7x7 or 7x6 lists of chars
def formatString(string):
    rowList = string.split('\r\n')
    newList = []
    for row in rowList:
        if(row == ''):
            continue
        newRow = row.split(' ')
        newNewRow = [i for i in newRow if i != ""]
        newList.append(newNewRow)

    return newList

#prints one row of the puzzle
def printRow(A, T, S, V, H, i):
    
    print("|", end="")
    for j in range(0, 7):
        num = ""
        sym = ""

        #print the existing entries and symbols
        if(T[i][j] != "0"):
            num = T[i][j]
            if(S[i][j] != "0"):
                if(S[i][j] == "1"):
                    sym == ""
                else:
                    sym = S[i][j]

            print((num + sym).ljust(4, " "), end="")
        else:
            print("    ", end="")
    
        #print the vertical barriers
        if(j != 6):
            if(V[i][j] != "0"):
                print("|", end="")
            else:
                print(" ", end="")
        
    print("|", end="")
    print()

    #print the horizonal barriers on the line below
    for j in range(0, 7):
        if(i < 6):
            if(H[j][i] != "0"):
                print(" ----", end="")
            else:
                print("     ", end="")
        
    if(i != 6):
        print()


#print the kenken puzzle (in a pretty way!)
def printPuzzle(A, T, S, V, H):
    #unsolved
    print(" ---- ---- ---- ---- ---- ---- ---- ")
    for i in range(0, 7):
        printRow(A, T, S, V, H, i)
    print(" ---- ---- ---- ---- ---- ---- ---- ")

#parses json data into separate string matricies
def parsePuzzle(puzzle):
    puzzle = puzzle.split('A')
    puzzle = puzzle[1].split('T')
    A = puzzle[0]
    puzzle = puzzle[1].split('S')
    T = puzzle[0]
    puzzle = puzzle[1].split('V')
    S = puzzle[0]
    puzzle = puzzle[1].split('H')
    V = puzzle[0]
    H = puzzle[1]

    A = formatString(A)
    T = formatString(T)
    S = formatString(S)
    V = formatString(V)
    H = formatString(H)

    printPuzzle(A, T, S, V, H)

def main():

    #read data from json file
    if len(sys.argv) != 2:
        print("Invalid syntax. ./pp <puzzle file json>")
        exit()
    with open(sys.argv[1], 'r') as fInput:
        data = json.load(fInput)
        parsePuzzle(data['data'])

main()
