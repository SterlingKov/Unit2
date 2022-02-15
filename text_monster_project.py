

dungeon = [
    ['sword', 'monster', 'sword', 'stairs up', 'empty'],
    ['sword', 'magic stone', 'stairs down', 'monster', 'stairs up'],
    ['magic stone', 'stairs down', 'empty', 'boss monster', 'prize']
]



current_floor = 0
current_room = 0
location = dungeon[current_floor][current_room]


inventory = []



while True:
    move_finished = True
    print(f"you are located in: {location}")
    move_input = input("What would you like to do? -left- -right- -up- -down- -fight- -run- -grab- -help-")

        
    if move_input == 'left': 
        current_room -= 1
        location = dungeon[current_floor][current_room]
        
        if current_room == -1:
            current_room += 1
            print("You can't move any further in that direction")
    
    elif move_input == 'right':
        current_room += 1
        location = dungeon[current_floor][current_room]
        
        if current_room == 5:
            current_room -= 1
            print("You can't move any further in that direction")

    elif move_input == 'up':
        if location == 'stairs up':
            current_floor += 1
            location = dungeon[current_floor][current_room]
            print(location)
            if current_floor == 3:
                current_floor -= 1
                print("You can't climb any higher!")
        else: 
            print("You can't go up...")

    elif move_input == 'down':
        if location == 'stairs down':
            current_floor -= 1
            location = dungeon[current_floor][current_room]
            print(location)
            if current_floor == -1:
                current_floor += 1
                print("You can't dig any deeper!")
        else: 
            print("You can't go down...")
    

    if location == 'monster':
        location = dungeon[current_floor][current_room] 
        move_input = input("You've encountered a dangerous monster. What would you like to do? -fight- -run-")
        if move_input == 'fight':
            if 'sword' in inventory:
                inventory.pop(inventory.index('sword'))
                print("You have slain the monster!")
                location = 'empty'
                move_finished = False
            else:
                print("You didn't have a sword, and thus you have died.")
                print("YOU LOST")
                break
        elif move_input == 'run':
            current_room -= 1
            print("You were able to escape from the monster")
            location = dungeon[current_floor][current_room]
            print(location)
            move_finished = False
        else:
            print("Enter a valid input")

    elif move_input == 'grab':
        if location == 'sword':
            inventory.append('sword')
            location = 'empty'
        elif location == 'magic stones':
            inventory.append('magic stones')
        else:
            print('There is nothing to grab')

    else:
        print("not valid")
                
        
