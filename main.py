import random
import sys
import os

class roll_dice:
    def __init__(self):
        # Set the dice configuration
        self.dice = [1, 2, 3, 4, 5, 6]


    def gameplay(self):
        # Refresh the display
        os.system('cls')
        # Welcome
        print("Welcome to Roll the Dice!")

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
        print("~~~~~~~~ RESULTS ~~~~~~~~")
        roll_dice().rolling(self.amount_rolls)


    def rolling(self, times):
        counter = 0
        while counter < times:
            self.roll = random.randint(self.dice[0], self.dice[-1])
            print(self.roll)
            counter += 1


if __name__ == '__main__':
    while True:
        game = roll_dice()
        game.gameplay()
        # Ask the user to continue run the game
        continue_rolling = input("\nRun again? [y/n]:-")
        if continue_rolling == 'y' or continue_rolling == 'yes':
            continue
        else:
            os.system('cls') 
            sys.exit()