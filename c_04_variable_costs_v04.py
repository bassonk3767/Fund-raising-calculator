# Imports...
import pandas as pd


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

# Gets expense, returns list which has
# the data frame and subtotal
def get_expenses(var_fixed):

    # Lowering case of the variable to
    # in-rich programming usability
    var_fixed.lower()

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

    item_name = ""

    # Loop to get component, quantity and price
    while item_name.lower() != "xxx":

        # Get name, quantity and item
        item_name = not_blank("\nItem name\n~~~ ",
                              "\nThe component name"
                              " can't be blank")

        if item_name == "xxx":
            retun item_name

        if var_fixed == "variable":
            quantity = num_check("Quantity\n~~~ ",
                                 "The amount must be a whole "
                                 "number, try again\n~~~ ",
                                 int)

        else:
            quantity = 1

        price = num_check("\nHow much for a singular item "
                          "(enter without currency signs)\n~~~ ",
                          "\nThe price must be a number"
                          " more than 0", float)

        # Add item, quantity and price to list
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)


# RECYCLED FUNCTIONS

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


# Currency formatting function
def currency(x):
    return f"${x:.2f}"



# Main routine...

# Get product name
product_name = not_blank("\nProduct name\n~~~ ",
                         "The product name "
                         "shouldn't be blank.")

# Get variable costs
variable_expense = get_expenses("variable")
variable_frame = variable_expense[0]
variable_sub = variable_expense[1]

# Get fixed costs
fixed_expenses = get_expense("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]

# *** Printing area ***

print(f"\n{fixed_frame[['Cost']]}")
print(f"Fixed costs: ${fixed:.2f}")

print(f"\n{fixed_frame['Cost']}\n")