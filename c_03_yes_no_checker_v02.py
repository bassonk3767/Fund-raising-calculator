# Imports...


# Functions...

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

# Looping to make testing faster
for item in range(0,6):
    want_help = yes_no("\nDo you want to read the instructions?\n~~~ ")
    print("\nYou said '{}'\n".format(want_help))
