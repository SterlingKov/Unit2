'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: itll print 0 a lot
actual:

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
actual:

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''
TTTboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turnNum = 0
while turnNum < 10:
    print("Tic Tac Toe Board")
    print(f"{TTTboard[0]} | {TTTboard[1]} | {TTTboard[2]} \n --------- \n{TTTboard[3]} | {TTTboard[4]} | {TTTboard[5]} \n---------- \n{TTTboard[6]} | {TTTboard[7]} | {TTTboard[8]}")

    square = int(input("Which square would you like to choose?: "))
    while TTTboard[square - 1] == 'X' or TTTboard[square - 1] == 'O':
        square = int(input("Which square would you like to choose?: "))
    if turnNum == 0 or 2 or 4 or 6 or 8:
        TTTboard[square - 1] = 'X'
    else:
        TTTboard[square - 1] = 'O'
    print(f"{TTTboard[0]} | {TTTboard[1]} | {TTTboard[2]} \n --------- \n{TTTboard[3]} | {TTTboard[4]} | {TTTboard[5]} \n---------- \n{TTTboard[6]} | {TTTboard[7]} | {TTTboard[8]}")
    turnNum = turnNum + 1