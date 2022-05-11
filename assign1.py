# Assignment 1 CSCI 2304 Intelligent Systems Section 1
# Nur Airin Faqihah Binti Ruzaidi 2011976
# Alya Aqilah Binti Ahmad Kamran 2011192

import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X" 
winner = None
gameRunning = True

# create board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input 
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else: 
        print("Oh no, the space is no longer empty! Try a again please T_T")

# check win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[6]
        return True

def checkRow(board): 
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[2]
        return True

def checkDiagonal(board): 
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board: 
        printBoard(board)
        print("My oh my! It is a tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")
        gameRunning = False 

# switch player
def switchPlayer(): 
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else: 
        currentPlayer = "X"

# computer input
def comp(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()

# check win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    comp(board)
    checkWin()
    checkTie(board)