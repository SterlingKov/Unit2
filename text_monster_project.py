

dungeon = [
    ['empty', 'monster', 'sword', 'stairs up', 'sword'],
    ['sword', 'magic stone', 'stairs down', 'monster', 'stairs up'],
    ['magic stone', 'stairs down', 'empty', 'boss monster', 'prize']
]



current_floor = 0
current_room = 0
location = dungeon[current_floor][current_room]
print(location)

inventory = []



while True:
    move_finished = True
    
    move_input = input("What would you like to do? -left- -right- -up- -down- -grab- -fight- -help-")

    if move_input == 'left':
        current_room -= 1
        print(location)
        if current_room == -1:
            current_room += 1
            print("You can't move any further in that direction")
    
    if move_input == 'right':
        current_room += 1
        print(location)
        if current_room == 5:
            current_room -= 1
            print("You can't move any further in that direction")

    if move_input == 'up':
        if location == 'stairs up':
            current_floor += 1
            print(location)
            if current_floor == 3:
                current_floor -= 1
                print("You can't climb any higher!")
        else: 
            print("You can't go up...")

    if move_input == 'down':
        if location == 'stairs down':
            current_floor -= 1
            print(location)
            if current_floor == -1:
                current_floor += 1
                print("You can't dig any deeper!")
        else: 
            print("You can't go down...")
    

    if location == 'monster':
        print(location)
        while move_finished:
            move_input = input("You've encountered a dangerous monster. What would you like to do? -fight- -run-")
            if move_input == 'fight':
                if inventory.index('sword') > -1:
                    inventory.pop(inventory.index('sword'))
                    print("You have slain the monster!")
                    move_finished = False
                else:
                    print("You didn't have a sword, and thus you have died.")
                    print("YOU LOST")
                    break
            elif move_input == 'run':
                current_room -= 1
                print("You were able to escape from the monster")
                print(location)
                move_finished = False
            else:
                print("Enter a valid input")
