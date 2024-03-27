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

        if var_fixed == "variable":
            quantity = num_check("Quantity\n~~~ ",
                                 "The amount must be a whole "
                                 "number, try again\n~~~ ",
                                 int)

        else:
            quantity = 1

        price = num_check("\nHow much for a singular item?\n~~~ ",
                          "\nThe price must be a number"
                          " more than 0", float)

        # Add item, quantity and price to list
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    variable_frame = pd.DataFrame(variable_dict)
    variable_frame = variable_frame.set_index("Item")

    # Calculate cost of each component
    variable_frame["Cost"] = variable_frame["Quantity"] \
                             * variable_frame["price"]

    # Find subtotal
    variable_sub = variable_frame["Cost"].sum()

    # Currency formatting (use currency function)
    add_dollars = ["Price", "Cost"]
    for item in add_dollars:
        variable_frame[item] = variable_frame[item].apply(currency)

    return [expense_frame, sub_total]


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

variable_expense = get_expenses("variable")
variable_frame = variable_expense[0]
variable_sub = variable_expense[1]

# *** Printing area ***

print("\n{}\n".format(fixed_frame[["Cost"]]))
print("Fixed costs: ${:.2f}".format(fixed_sub))

print(f"\n{fixed_frame['Cost']}\n")