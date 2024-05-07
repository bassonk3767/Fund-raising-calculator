# Imports...
import math as ma


# Functions...

# multy number type checker
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(eror)
            else:
                return response

        except ValueError:
            print(error)


# Rounding function
def round_up(amount, round_to):
    return int(ma.ceil(amount / round_to) * round_to)


# RECYCLED CODE

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


# Checks if user input is blank
def not_blank(question, error):

    # Looping to get user's answer
    while True:

        # The user's input
        response = input(question).strip()

        # Checking if user has entered empty text
        if response == "":
            print(f"{error}, Please try again")
        else:
            return response


# Main routine...

# Get the amount of the user's product
how_many = num_check("\n\nHow many items?\n~~~ ",
                     "\n\nIt can't be 0", int)

# Get the total price of the user's product(s)
total = num_check("\n\n What is the total cost?\n~~~ ",
                   "\n\nIt has to be more than 0",int)

# Get the user's profit goal
profit_goal = num_check("\n\nWhat is the profit goal?\n~~~ ",
                        "It has to be more than 0", int)

# Get the number that the user would like to round to
round_to = num_check("\n\nWhat should the amounts "
                    "be rounded to?\n~~~ ", "\n\nIt can't be 0",
                    int)

sales_needed = total + profit_goal

print(f"\n\nTotal: ${total}")
print(f"\nProfit goal: ${profit_goal}")

selling_price = sales_needed / how_many
print(f"\n\nSelling price: ${selling_price}")


recommended_price = round_up(selling_price, round_to)
print(f"\nSelling price (rounded to the nearest "
      f"{round_to}): ${recommended_price}")

to_round = [2.75, 2.25, 2]

for item in to_round:
    rounded = round_up(item, 1)
    print(f"\n\n${item:.2f} --> ${rounded:.2f}")
