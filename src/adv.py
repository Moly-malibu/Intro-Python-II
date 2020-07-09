from room import Room
from item import Item
from player import Player
from time import sleep
from textwrap import wrap

# Declare all the rooms

room = {
    'outside': Room(
        name="Outside Cave Entrance",
        description="North of you, the cave mouth beckons",
        items=[]
    ),
    'foyer': Room(
        name="Foyer", 
        description="""Dim light filters in from the south. Dusty passages run north and east.""",
        items=[]
    ),
    'overlook': Room(
        name="Grand Overlook", 
        description="""A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
        items=[]
    ),
    'narrow': Room(
        name="Narrow Passage", 
        description="""The narrow passage bends here from west to north. The smell of gold permeates the air.""",
        items=[]
    ),
    'treasure': Room(
        name="Treasure Chamber", 
        description="""You've found the long-lost treasure chamber! Sadly, it has  already been completely emptied by earlier adventurers. The only exit is to the south.""",
        items=[]
    ),
}
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
print(type(room['foyer']))

# Main
# Write a loop that:
if __name__=="__main__": 
    name = input("Input your name:")  # * Prints the current room name
    player = Player(name, room["outside"]) # Make a new player object that is currently in the 'outside' room.
    
    for i in range(3):
        print(',')
        sleep(0.15)
    while True:
        print('', '---', '', sep='\n')
        print(player.current_room.name.upper())
        for A in wrap(player.current_room.description, 100):
            print (A)
# * Prints the current description (the textwrap module might be useful here).

        if player.current_room.items:
            print('\n Items: ')
            for item in player.current_room.items:
                print(f' {item.name}: {item.description}') 
        current_desc = input('> ').lower().split(' ')
        verb = current_desc[0]
        if verb in ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']:
            player.move(verb[0])
            continue
 # * Waits for user input and decides what to do.   
 # If the user enters a cardinal direction, attempt to move to the room there.
 # Print an error message if the movement isn't allowed.

        elif verb in ['get', 'take', 'drop']:
            if len(current_desc) < 2:
                print(f'Enter an object to {verb}.')
                input('\n --Enter any key to continue--')
                continue
            object = current_desc[1]
            if verb == 'drop':
                drop_item, drop_idy = None, None
                for idy, item in enumerate(player.items):
                    if object == item.name.lower():
                        drop_idy = idy
                        drop_item = item
            if not drop_item:
                print('out Item')
            else:
                player.current_room.items.append(
                    player.items.pop(idy)
                )
                drop_item.on_drop()
        elif verb in ['get', 'take']:
            take_time, take_idy = None, None
            for idy, item in enumerate(player.current_room.items):
                if object == item.name.lower():
                    take_idy = idy
                    take_item = item
            if not take_item:
                print("Room out items.")
            else:
                player.items.append(
                    player.current_room.items.pop(idy)
                )
                take_item.on_take()
        elif verb == 'inventory':
            if player.items:
                for item in player.items:
                    print(f' {item.name}: {item.description}')
            else:
                print("Out Items")

# If the user enters "q", quit the game.        
        elif verb == 'q':
            break
        else:
            print('Direction: Position (n/e/s/w) or take/drop/inventory')
        input('\n -- Enter any Key to Continue--')
        continue