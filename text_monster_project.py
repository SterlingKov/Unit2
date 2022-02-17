

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
    
    print(f"you are located in: {location}")
    move_input = input("What would you like to do? -left- -right- -up- -down- -fight- -run- -grab- -inventory- -help- ")

    if move_input == 'help':
        print("left - goes to the room to the left \n" 
        "right - goes to the room to the right \n"
        "up - can only be used on 'stairs up' \n"
        "down - can only be used on 'stairs down' \n"
        "fight - use this command to fight a monster \n"
        "run - can be used to run away from a monster \n"
        "grab - used to pick up swords and magic stones \n"
        "inventory - allows you to see everything in your inventory"
        )

    if move_input == 'inventory':
        print(inventory)

    if move_input == 'left': 
        current_room -= 1
        if current_room == -1:
            current_room += 1
            location = dungeon[current_floor][current_room]
            print("You can't move any further in that direction")
        else:
            location = dungeon[current_floor][current_room]
    
    elif move_input == 'right':
        current_room += 1
        if current_room == 5:
            current_room -= 1
            location = dungeon[current_floor][current_room]
            print("You can't move any further in that direction")
        else:
            location = dungeon[current_floor][current_room]

    elif move_input == 'up':
        if location == 'stairs up':
            current_floor += 1
            current_room = 0
            if current_floor == 3:
                current_floor -= 1
                location = dungeon[current_floor][current_room]
                print("You can't climb any higher!")
            else:
                location = dungeon[current_floor][current_room]
        else: 
            print("You can't go up...")

    elif move_input == 'down':
        if location == 'stairs down':
            current_floor -= 1
            if current_floor == -1:
                current_floor += 1
                print("You can't dig any deeper!")
            else:
                location = dungeon[current_floor][current_room]
        else: 
            print("You can't go down...")
    

    if location == 'monster':
        location = dungeon[current_floor][current_room] 
        move_input = input("You've encountered a dangerous monster. What would you like to do? -fight- -run- ")
        if move_input == 'fight':
            if 'sword' in inventory:
                inventory.pop(inventory.index('sword'))
                print("You have slain the monster!")
                location = 'empty'
                dungeon[current_floor][current_room] = 'empty'
            else:
                print("You didn't have a sword, and thus you have died.")
                print("YOU LOST")
                break
        elif move_input == 'run':
            current_room -= 1
            print("You were able to escape from the monster")
            location = dungeon[current_floor][current_room]
        else:
            print("Enter a valid input")

    elif move_input == 'grab':
        if location == 'sword' and len(inventory) < 4:
            inventory.append('sword')
            location = 'empty'
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'magic stone' and len(inventory) < 4:
            inventory.append('magic stone')
            location = 'empty'
            dungeon[current_floor][current_room] = 'empty'
        elif len(inventory) > 3:
            print("You cannot hold any more items")
        else:
            print('There is nothing to grab')

    if location == 'boss monster':
        location = dungeon[current_floor][current_room]
        print("You've encountered the BOSS MONSTER. YOU MUST FIGHT TO THE DEATH!")
        if 'sword' in inventory and 'magic stone' in inventory:
            input("*hit enter to continue*")
            print("THE BOSS HAS BEEN DEFEATED")
            input('')
            location = 'empty'
            dungeon[current_floor][current_room] = 'empty'
        else:
            print("You have come unprepared. YOU LOST")
            break
    
    if location == 'prize':
        location = dungeon[current_floor][current_room]
        move_input = input("You have encountered the prize. You must grab it. ")
        if move_input == 'grab':
            print("You have grabbed the prize. You have won.")
            break
        else:
            print("IDIOT. You missed the prize. You lost...")
            break