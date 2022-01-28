'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------

a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")


Prediction: If you say to seek a holy grail, then it will ask you the velocity of an unladen swallow. If you say something besides the expected response, it'll throw you off the bridge. If you get it right, it'll throw the bridge keeper of the bridge. If you say something else besides that, it'll say go on. off you go
Actual:

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: if you name a color listed it'll say something back about the color. Anything else will say I dont recognize that color.
Actual:

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:
'''
'''
x = int(input("what is x? "))
y = int(input("what is y? "))
z = int(input("what is z? "))
if x + y > z and x + z > y and y + z > x:
    print("perimiter of the triangle is " + str(x + y + z))
if(x * x + y * y == z * z):
    print("this is a right triangle")
    if(x == y and y == z):
        print("this is an equillateral triangle")
    elif(z == x or z == y or x == y):
        print("this is an isosceles triangle")
    else:
        print("this is a scalene triangle")
else:
    print("not a triangle")
'''
'''
---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
prize1 = "BMW"
prize2 = "apple"
prize3 = "phone"
prize4 = "saxophone"
prize5 = "telegram from 1850"
prize6 = "dog"
prize7 = "desk"
prize8 = "computer"
prize9 = "poster"
prize10 = "glasses"

user_prize = int(input("Pick a number 1-10: "))
if user_prize == 1:
    print(prize1)
elif user_prize == 2:
    print(prize2)
elif user_prize == 3:
    print(prize3)
elif user_prize == 4:
    print(prize4)
elif user_prize == 5:
    print(prize5)
elif user_prize == 6:
    print(prize6)
elif user_prize == 7:
    print(prize7)
elif user_prize == 8:
    print(prize8)
elif user_prize == 9:
    print(prize9)
else:
    print(prize10)