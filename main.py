import random
import sys
import os

# Refactor the code
# Switch the dice art to an extern file

class roll_dice:
    def __init__(self):
        # Set the dice configuration
        self.dice = [1, 2, 3, 4, 5, 6]
        self.dice_art = {
            1: (
                "┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘",
                ),
            2: (
                "┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘",
                ),
            3: (
                "┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘",
                ),
            4: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘",
                ),
            5: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘",
                ),
            6: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘",
                ),
            }
        self.die_height = len(self.dice_art[1])
        self.die_width = len(self.dice_art[1][0])
        self.die_face_separator = " "


    def gameplay(self):
        '''Introduction to the game, the input for the user and the handling errors'''
        # Refresh the display
        os.system('cls')
        # Welcome
        print("~~~~~~~~~~~~~~ Roll the Dice ~~~~~~~~~~~~~~\n")

        while True:
            # Handling input errors, out of the range and strings
            try:
                # How many rolls do?
                self.amount_rolls = int(input("How many dice do you want to roll? [1-6]:-"))

                if self.amount_rolls in range(self.dice[0], self.dice[-1]+1):
                    break
                else:
                    os.system('cls')
                    print('Follow the range')
                    continue

            except ValueError:
                os.system('cls')
                print('ONLY NUMBERS')
                continue

        os.system('cls')
        roll_dice().generate_dice_faces_diagram(self.amount_rolls)


    def rolling(self, times):
        '''Set a counter in 0, increase by 1 until the counter it's equal to the rolling times. During this, the while loop will generate a random roll and append it to the roll result list.'''
        counter = 0
        # Empty list for the results
        self.roll_result = []
        while counter < times:
            self.roll = random.randint(self.dice[0], self.dice[-1])
            self.roll_result.append(self.roll)
            counter += 1
        roll_dice().generate_dice_faces_diagram(self.roll_result)

    
    def generate_dice_faces_diagram(self, times):
        """Return an ASCII diagram of dice faces from `roll_result`."""
        counter = 0
        # Empty list for the results
        self.roll_result = []
        while counter < times:
            self.roll = random.randint(self.dice[0], self.dice[-1])
            self.roll_result.append(self.roll)
            counter += 1

        # Generate a list of dice faces from DICE_ART
        self.dice_faces = []
        for value in self.roll_result:
            self.dice_faces.append(self.dice_art[value])

        # Generate a list containing the dice faces rows
        self.dice_faces_rows = []
        for row_idx in range(self.die_height):
            self.row_components = []
            for die in self.dice_faces:
                self.row_components.append(die[row_idx])
            self.row_string = self.die_face_separator.join(self.row_components)
            self.dice_faces_rows.append(self.row_string)

        # Generate header with the word "RESULTS" centered
        self.width = len(self.dice_faces_rows[0])
        self.diagram_header = " RESULTS ".center(self.width, "~")

        self.dice_faces_diagram = "\n".join([self.diagram_header] + self.dice_faces_rows)
        print(self.dice_faces_diagram)


if __name__ == '__main__':
    while True:
        game = roll_dice()
        game.gameplay()
        # Ask the user to continue run the app
        continue_rolling = input("\nRun again? [y/n]:-")
        if continue_rolling == 'y' or continue_rolling == 'yes':
            continue
        else:
            os.system('cls') 
            sys.exit()