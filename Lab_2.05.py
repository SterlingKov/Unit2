'''
############################
Lab 2.05 - Tic-Tac-Toe
############################
In your Notebook
1. Predict what will be printed. Then run the program and confirm
Example 1
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[0:3])
print(a[1:4])

Prediction: a, b, c || b, c, d
Actual:

Example 2
---------
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:len(a) - 3])

Prediction: a, b
Actual:

Example 3
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.remove('b')
print(a)
print(b)

Prediction: a, b, c, d, e || a, c, d, e
Actual:

Example 4
---------
a = ['a', 'b', 'c', 'd', 'e']
a[0] = 'haha'
b = a.pop()
print(a)
print(b)

Prediction: haha, b, c, d, e || b, c, d, e
Actual: haha, b, c, d, e || e

Example 5
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a + ['abc']
print(a)
print(b)

Prediction: a, b, c, d, e || a, b, c, d, e, abc
Actual:

Example 6
---------
a = ['a', 'b', 'c', 'd', 'e']
b = a.append('f')
print(a)
print(b)

Prediction: a, b, c, d, e || a, b, c, d, e, f
Actual: a, b, c, d, e || None
2. In script mode (Type your program below the multi-line comment)
We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect
that.
    Example:
        1 | 2 | 3
        ---------
        4 | 5 | X
        ---------
        7 | 8 | 9
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
'''
print("Tic Tac Toe Board")
TTTboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{TTTboard[0]} | {TTTboard[1]} | {TTTboard[2]} \n --------- \n{TTTboard[3]} | {TTTboard[4]} | {TTTboard[5]} \n---------- \n{TTTboard[6]} | {TTTboard[7]} | {TTTboard[8]}")

Xsquare = int(input("Which square would you like to choose?: "))
TTTboard[Xsquare - 1] = 'X'
print(f"{TTTboard[0]} | {TTTboard[1]} | {TTTboard[2]} \n --------- \n{TTTboard[3]} | {TTTboard[4]} | {TTTboard[5]} \n---------- \n{TTTboard[6]} | {TTTboard[7]} | {TTTboard[8]}")