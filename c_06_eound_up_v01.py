# Imports...
import math as ma


# Functions...

# Rounding function
def round_up(amount, round_to):
    return int(ma.ceil(amount / round_to) * round_to)


# Checks the user's response
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("\nPlease enter either yes or no\n")


# Main routine...

# VIDEO 28

to_round = [2.75, 2.25, 2]

for item in to_round:
    rounded = round_up(item, 1)
    print(f"\n\n${item:.2f} --> ${rounded:.2f}")
