#!/usr/bin/env python3

puzzle = "A\r\n4 1 2 3 5 7 6 \r\n6 4 7 2 1 3 5 \r\n5 2 1 7 4 6 3 \r\n7 3 4 1 6 5 2 \r\n3 7 6 5 2 1 4 \r\n2 5 3 6 7 4 1 \r\n1 6 5 4 3 2 7 \r\nT\r\n 10   3   0   8   0  18   0\r\n  0  11   0   3   0   3   0\r\n 12   5  12   0   4   9   0\r\n  0   0   0   6  11   0   6\r\n 10   0   9   0   3   0   0\r\n  7   0   0  13   0   6   8\r\n  7   0   5   7   0   0   0\r\nS\r\n+ + 0 + 0 + 0\r\n0 + 0 + 0 1 0\r\n+ + + 0 1 + 0\r\n0 0 0 + + 0 +\r\n+ 0 + 0 + 0 0\r\n+ 0 0 + 0 + +\r\n+ 0 1 + 0 0 0\r\nV\r\n1 0 1 0 1 0\r\n1 0 1 0 1 1\r\n1 1 0 1 1 0\r\n1 1 1 1 0 1\r\n0 1 1 1 0 1\r\n0 1 1 0 1 1\r\n0 1 1 0 1 1\r\nH\r\n0 1 0 1 1 1\r\n1 1 0 1 1 1\r\n1 1 0 1 0 1\r\n1 1 1 0 1 1\r\n1 1 1 1 1 1\r\n1 1 1 1 1 0\r\n0 1 1 0 1 0\r\n\r\n"

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

def printRow(A, T, S, V, H, i):
    
    print("|", end="")
    for j in range(0, 7):
        num = ""
        sym = ""
        if(T[i][j] != "0"):
            # print(T[i][j], end="")
            num = T[i][j]
            if(S[i][j] != "0"):
                #print(S[i][j].ljust(2, " "), end="")
                sym = S[i][j]

            print((num + sym).ljust(4, " "), end="")
        else:
            print("    ", end="")
    

        #print((num + sym).ljust(4, " "), end="")

        if(j != 6):
            if(V[i][j] != "0"):
                print("|", end="")
            else:
                print(" ", end="")
        
        
    print("|", end="")
    print()

    for j in range(0, 6):
        
        if(H[j][i] != "0"):
            print(" ----", end="")
        else:
            print("     ", end="")
        
    
    print()


def printPuzzle(A, T, S, V, H):
    #unsolved
    for i in range(0, 7):
        if(i == 0):
            print(" ---- ---- ---- ---- ---- ---- ---- ")
        printRow(A, T, S, V, H, i)
       


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

    print(A)
    print(T)
    print(S)
    print(V)
    print(H)

    A = formatString(A)
    T = formatString(T)
    S = formatString(S)
    V = formatString(V)
    H = formatString(H)

    print(H[6][5])

    printPuzzle(A, T, S, V, H)


parsePuzzle(puzzle)

