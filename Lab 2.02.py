'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
                 
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction:  True                   Actual:
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction:   False                  Actual:
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction:    True                 Actual:
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction: no clue                    Actual: False

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y

not(x and y) == not x or not y
'''

#president test
'''
print("I Can't be President?!")
age = input("Enter your age: ")
us_residual_length = input("Enter how long you've lived in the us: ")
natural_born = input("Were you born in the US? (Y/N): ")

if int(age) > 35 and int(us_residual_length) >= 14 and natural_born == 'Y':
    print(False)
    print("You have met all the requirements to become president")
else:
    print(True)
    print("You are not allowed to be president")
'''
#roller coaster check
'''
print("Can I ride the roller coaster?")
height = input("How tall are you in inches? ")
age = input("How old are you? ")
num_of_quarters = input("How many quarters do you have? ")
freq_rider_pass = input("Do you have the frequent rider pass? (Y/N) ")

if int(height) > 50 or int(age) >= 18:
    if freq_rider_pass == "Y":
        if int(num_of_quarters) >= 2:
            print(True)
        if int(num_of_quarters) < 2:
            print(False)
    if freq_rider_pass == "N":
        if int(num_of_quarters) >= 4:
            print(True)
else:
    print(False)
'''
#DeMorgan's law thing
'''
According to DeMorgan's law, not(x or y) == not x and not y and not(x and y) == not x or not y are both equal. Idk why I don't know calculus but it said so on the website.
'''