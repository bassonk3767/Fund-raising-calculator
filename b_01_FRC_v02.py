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
                print(error)
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
            break

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

    expense_frame = pd.DataFrame(variable_dict)

    sub_total = expense_frame["Price"].sum()

    return expense_frame, sub_total


# Prints the expenses of the user
def expense_print(heading, frame, subtotal):
    pritn(f"\n**** {heading} Costs ****\n\n")
    print(f"{frame}\n\n{heading} Costs: ${subtotal:.2f}")

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


# Yes no checker
def yes_no(question):

    # Looping to get the user's answer
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("\nPlease answer yes / no")


# Main routine...


# Get product name
product_name = not_blank("\nProduct name\n~~~ ",
                         "The product name "
                         "shouldn't be blank.")

print("\nPlease enter your variable costs below\n")

# Get variable costs
variable_expense = get_expenses("variable")
variable_frame = variable_expense[0]
variable_sub = variable_expense[1]

have_fixed = yes_no("\nDo you have fixed costs? y/n\n~~~ ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
