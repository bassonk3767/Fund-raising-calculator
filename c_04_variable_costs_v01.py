# Imports...
import pandas as pd


# Functions...

# multy number type checker
def num_check(question, error, num_type):
    valid = false
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(eror)
            else:
                return response

        except ValueError:
            print(error)


# RECYCLED FUNCTIONS

# Checks if user input is blank
def not_blank(question, error):

    # Looping to get user's answer
    while True:

        # The user's input
        response = input(question).strip()

        # Checking if user has entered empty text
        if response == "":
            print("{}, Please try again".format(error))
        else:
            return response


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main routine...

# Setting up lists and dictionaries

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

error = "\nThe product name can't be blank"

# Get user data
product_name = not_blank("\nProduct name\n~~~ ", error)

item_name = ""

# Loop to get component, quantity and price
while item_name.lower() != "xxx":

    # Get name, quantity and item
    item_name = not_blank("\nItem name\n~~~ ",
                          "\nThe component name"
                          " can't be blank")

    if item_name == "xxx":
        break

    quantity = num_check("\nQuantity\n~~~ ",
                         "The amount must be"
                         " a whole number.", int)

    price = num_check("\nHow much for a singular item?",
                      "\nThe price must be a number"
                      " more than 0", float)