# File:       Autofill.py
# Author:     Hemang Bhatt
# Date:       12/07/15

# Description:
# This file contains code of autofill program that will ask user to provide
# a point in gird, and will "fill" the entire space it belongs to using a
# character provided by the user.


# This function will print the board using for loop
def printBoard(board):
    print()
    for row in range(len(board)):
        for column in range(len(board[row])):
            print(board[row][column], end = "")
        print()

# This function is recursive and it will fill the empty space of the board by
# character provided by user

def autoFill(row, column, board, symbol, printCondition):

    # DO NOTHING IF THE SPACE IS NOT EMPTY (BASE CASE)
    if board[row][column] != ' ':
        return board
    # Fill the board with the symbol in empty space
    if (board[row][column] == ' '):
        board[row][column] = symbol

        # this condition will print board in each recursive step.
        if printCondition == "yes":
            printBoard(board)
    
        # cell above current one
        if row > 0:
            autoFill(row-1, column, board, symbol, printCondition)
        # cell to the right
        if column < len(board[0]) - 1:
            autoFill(row, column + 1, board, symbol, printCondition)
        # cell below the current one
        if row < len(board) - 1:
            autoFill(row + 1, column, board, symbol, printCondition)
        # cell to the left one
        if column > 0:
            autoFill(row, column - 1, board, symbol, printCondition)
    return board
    
    
def main():

    fileName = input("Please enter a file for input: ")
    EXT1 = ".dat"
    EXT2 = ".txt"
    # filter the extension of file
    extension = fileName[-4:]

    # while loop to check extension
    while not ((extension == EXT1) or (extension == EXT2)):
        fileName = input("That is not a valid file -- please enter a filename \n\t that ends in \".dat\" or \".txt\": ")
        extension = fileName[-4:]

    # Open file for reading    
    openFile = open(fileName)
    myFile = openFile.readlines()
    board = []
    stripLine = ""
    
    # for loop to store file in 2D List
    for line in range(len(myFile)):
        board.append([])
        stripLine = (myFile[line]).strip()
        for i in stripLine:
            board[line].append(i)
    printBoard(board)
    
    # Close open file
    openFile.close()
    # Maximum number of rows
    rows = len(board)
    # Maximum number of columns
    columns = len(board[0])    
    QUIT = "Q"
    coordinates = ""
    
    # Exit while loop when user enter Q
    while coordinates != QUIT:
        coordinates = input("Please enter the coordinates you would like to start\
\nfilling at in the form \"row,col\" or Q to quit: ")
        # If user enter Q, exit the program
        if coordinates == QUIT:
            print("Thank you for using the autofill program!")
            return

        # length of cordintaes will greater than one
        elif len(coordinates) > 1:

            coordinates = coordinates.split(',')
            row         = int(coordinates[0])
            column      = int(coordinates[1])
            
            # Check the validation of row
            if (row not in range(0, rows)):
                print(row, "is not a valid row value; please enter a number\
\n\tbetween 0 and", (rows - 1))

            # Input validation for column
            if (column not in range(0, columns)):
                print(column, "is not a valid column value; please enter a number\
\n\tbetween 0 and", (columns - 1))
            
            # if row and column in proper range of board
            elif ((row in range(0, rows)) and (column in range(0, columns))):
                symbol = input("Please enter a symbol to fill with: ")
                # Check the length of symbol
                while len(symbol) != 1:
                    print("The symbol", "\"" + symbol + "\"", "is not a single chracter.")
                    symbol = input("Please enter a symbol to fill with: ")
                printCondition = ""

                # ask for printBoard at each recursion
                while ((printCondition != "no") and (printCondition != "yes")):
                    printCondition = input("Would like to show each step of the recursion? \nEnter \"yes\" or \"no\": ")
                    if ((printCondition != "no") and (printCondition != "yes")):
                        print("The choice", "\"",printCondition,"\"", "is not valid.")

                # call the autoFill function
                board = autoFill(row, column, board, symbol, printCondition)
                print("=" * 30)
                coordinates = ""
                printBoard(board)
                print()
main()
