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

# Gets expense, returns list which has
# the data frame and subtotal
def get_expenses(var_fixed):


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

    # Add item, quantity and price to list
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pd.DataFrame(variable_dict)
variable_frame = variable_frame.set_index("Item")

# Calculate cost of each component
variable_frame["Cost"] = variable_frame["Quantity"]\
                         * variable_frame["price"]

# Find subtotal
variable_sub = variable_frame["Cost"].sum()

# Currency formatting (use currency function)
add_dollars = ["Price","Cost"]
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# *** Printing Area ***

print(variable_frame)
print("\nVariable_costs: $(:.2f)".format(variable_sub))