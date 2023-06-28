# Code by: Jaden Bryon Knutson

# GAMEPLAY MAIN FUNCTION:
def main():

# INNER FUNCTIONS:
    # Outputs the current location, inventory, room item, and directions.
    def user_status():
        # Outputs the current room and user inventory to the user.
        print(f"\n\nUSER STATUS:")
        print(f"""    Current Location:  {current_room}
    Current Inventory: {user_inventory}""")

        # Outputs the room item if user has not obtained it yet, otherwise room item will be blank.
        if current_item not in user_inventory:
            print(f"    Room Item:         [{current_item}]")
        else:
            print("    Room Item:         []")
        print("""\nCOMMANDS:
    To travel a direction type:  North, South, East, West
    To pickup an item type:      'Item Name'
    To exit the game type:       Exit\n""")

    # If an acceptable directional input is registered, a new item is retrieved from the dictionary using the direction.
    # Returns the new item to replace the current item variable.
    def get_new_item(current_item, direction):
        new_item = current_item

        for i in items:
            if i == current_item:
                if direction in items[i]:
                    new_item = items[i][direction]
        return new_item

    # If an acceptable directional input is registered, a new room is retrieved from the dictionary using the direction.
    # Returns the new room to replace the current room variable.
    def get_new_room(current_room, direction):
        new_room = current_room

        for i in rooms:
            if i == current_room:
                if direction in rooms[i]:
                    new_room = rooms[i][direction]
        return new_room

# STORED INFORMATION:
    # Dictionary of rooms and associated items.
    rooms = {
        'Counter Top': {'West': 'The City of Pots and Pans', 'Exit': 'Exit Room'},
        'The City of Pots and Pans': {'North': 'The Dishwasher Wetlands', 'East': 'Counter Top', 'Exit': 'Exit Room'},
        'The Dishwasher Wetlands': {'North': 'The Sketchy Snack Drawer', 'East': 'The Silverware Drawer of Solitude',
                                    'South': 'The City of Pots and Pans', 'West': 'The Forest of Spices', 'Exit': 'Exit Room'},
        'The Forest of Spices': {'East': 'The Dishwasher Wetlands', 'Exit': 'Exit Room'},
        'The Sketchy Snack Drawer': {'East': 'The Messy Microwave', 'South': 'The Dishwasher Wetlands', 'Exit': 'Exit Room'},
        'The Messy Microwave': {'West': 'The Sketchy Snack Drawer', 'Exit': 'Exit Room'},
        'The Silverware Drawer of Solitude': {'North': 'The Trash Can Kingdom', 'West': 'The Dishwasher Wetlands', 'Exit': 'Exit Room'},
        'The Trash Can Kingdom': {'South': 'The Silverware Drawer of Solitude', 'Exit': 'Exit Room'},
        'Exit Room': {}
    }
    items = {
        '': {'West': 'Raid Bug Spray'},
        'Raid Bug Spray': {'North': 'Sticky Pads', 'East': ''},
        'Sticky Pads': {'North': 'Insecticide Dust', 'East': 'Fly Swatter',
                        'South': 'Raid Bug Spray', 'West': 'Boric Acid'},
        'Boric Acid': {'East': 'Sticky Pads'},
        'Insecticide Dust': {'East': 'Plastic Wrap', 'South': 'Sticky Pads'},
        'Plastic Wrap': {'West': 'Insecticide Dust'},
        'Fly Swatter': {'North': 'King Cockroach', 'West': 'Sticky Pads'},
        'King CockRoach': {'South': 'Fly Swatter'},
    }

    # Assigns the starter room, item, inventory, and a boolean value while loop that loops the gameplay.
    user_inventory = []
    current_room = 'Counter Top'
    current_item = ""
    user_play = True

    # START: Welcome Message
    print("""\nYou have been shrunken down in your kitchen by King Cockroach!
     
To turn yourself back to normal you must:
    Find all 6 of your items that got scattered throughout the kitchen.
    Face off with King Cockroach in battle and reverse his shrink ray tech.

WARNING:
    Avoid running into King Cockroach before all items have been found.
--------------------------------------------------------------------------

(START GAME)""", end="")

# GAMEPLAY LOOP:
    # Loops our gameplay until the user finishes game or "exit" is typed in by user.
    while user_play == True:

        # If the user types in "Exit" it will retrieve the exit room from our dictionary and then end the game. END.
        if current_room == "Exit Room":
            print("""\n\nYou have exited the game. Thank you for playing!
               
(END GAME)""")
            break

        # If user enters the boss room, determine win or lose depending on number of items.
        if current_room == "The Trash Can Kingdom":

            # If the user hasn't found all of the items before facing the boss, they die. (END)
            if len(user_inventory) < 6:
                print("""\n\nYou tried to fight King Cockroach without your weapons. 
YOU DIED!
           
(END GAME)""")
                return direction == "Exit"

            # If the user has collected all items, output to user that they have won the game. (END)
            else:
                print("""\n\nYou came prepared and defeated King Cockroach. 
YOU WON! 
           
(END GAME)""")
                return direction == "Exit"

        # Outputs the current location, inventory, and room item.
        user_status()

        # Inputs a direction or instruction from user.
        direction = input("""    USER INPUT = """).title().strip()
        print("--------------------------------------------------------------------------")

        # If the user input is a viable direction, the functions returns a new room and item or exits the game.
        if direction == "North" or direction == "South" or direction == "East" or direction == "West" or direction == "Exit":
            new_room = get_new_room(current_room, direction)
            new_item = get_new_item(current_item, direction)

            # If the direction is not viable then output user runs nto a wall.
            if new_room == current_room:
                print("\nACTION:   You smacked into a wall. Choose another direction.", end="")


            # If the direction is viable, the current room and item are changed depending on the user input.
            else:
                current_room = new_room
                current_item = new_item

                # Outputs what room the user traveled to.
                print(f"\nACTION:   You traveled to the {current_room}.", end="")

        # If input is the current item, current item is not a blank string, and current item is not in user inventory:
        elif direction == current_item and current_item != "" and current_item != "King Cockroach" and current_item not in user_inventory:

            # Outputs what item the user has picked up
            print(f"\nAction:   You have picked up {current_item}.", end="")

            # Add the current item to our user inventory list.
            user_inventory.append(current_item)

        # If an invalid input is typed, output to user that input is invalid.
        else:
            print("\nACTION:   Invalid input. Please try again.", end="")

# GAMEPLAY FUNCTION CALL:
main()


