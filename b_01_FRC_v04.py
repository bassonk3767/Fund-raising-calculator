# Imports...
import pandas as pd
import math as ma

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
# def expense_print(heading, frame, subtotal):
#     print(f"\n**** {heading} Costs ****\n\n")
#     print(f"{frame}\n\n{heading} Costs: ${subtotal:.2f}")


# Finds the profit goal
def profit_goal(total_costs):
    amount = ""

    # Initialize variables and error message
    error = "\n\nPlease enter a valid profit gaol\n"

    valid = False
    while not valid:

        # Ask for profit goal...
        response = input("\n\nWhat is your profit goal? "
                         "(e.g. $500 or 37%)\nNote that "
                         "you are allowed to use currency"
                         " and percentage respectively\n~~~ ")

        # CHeck if first character is $
        if response[0] == "$":
            profit_type = "$"

            # Get amount (everything after $)
            amount = response[1:]

        # Check if last character is %
        elif response[-1] == "%":
            profit_type = "%"

            # Get amount (everything before %
            amount += response[-1]

        else:
            # set amount to response for now
            profit_type = "unknown"

        try:
            # Check amount is a number more than 0
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown":
            dollar_type = yes_no(f"\n\nDo you mean ${amount:.2f}."
                                 f"\nie {amount:.2f} dollars?\n~~~ ")

            # Set profit type based on user's answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"\n\nDo you mean {amount}%?, y/n\n~~~ ")

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Calculates the rounded value
# of a given number as input
def round_up(amount, round_to):
    return int(ma.ceil(amount / round_to)) * round_to


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


# Rounding function
def round_up(amount, round_to):
    return int(ma.ceil(amount / round_to) * round_to)


# Main routine...

# Get product name
product_name = not_blank("\nProduct name\n~~~ ",
                         "The product name "
                         "shouldn't be blank.")

# Get the amount of the user's product
how_many = num_check("\n\nHow many items?\n~~~ ",
                     "\n\nIt can't be 0", int)

print("\nPlease enter your variable costs below\n")

# Get variable costs
variable_expense = get_expenses("variable")
variable_frame = variable_expense[0]
variable_sub = variable_expense[1]

variable_frame_txt = pd.DataFrame.to_string(variable_frame)
variable_sub_txt = f"Variable Costs Subtotal: ${variable_sub:.2f}\n"

have_fixed = yes_no("\nDo you have fixed costs? y/n\n~~~ ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

    fixed_frame_txt = pd.DataFrame.to_string(fixed_frame)
    fixed_sub_txt = f"Fixed Costs Subtotal: ${fixed_sub:.2f}\n"

else:
    fixed_sub = 0

    fixed_frame_txt = ""
    fixed_sub_txt = ""

# Work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculate recommended price
# and then write th data to
# a separate file
total_costs = all_costs + profit_target
selling_price = total_costs / how_many

# round recommended price
recommended_price = round_up(selling_price,5)

heading = f"\n\n**** Fund Raising - {product_name} ****"
# expense_print("Variable", variable_frame, variable_sub)

variable_heading_txt = "\n==== Variable Costs ====="

if have_fixed == "yes":
    fixed_heading_txt = "\n===== Fixed Costs ======"
    #     expense_print("Fixed", fixed_frame[["Cost"]], fixed_sub)

else:
    fixed_heading_txt = ""

total_costs_str = f"\n\n**** Total Costs: ${profit_target:.2f} ****\n"
sales_advice_txt = "\n**** Profit & Sale Targets ****"

profit_target_txt = f"\n\n**** Profit Target: ${profit_target:.2f}"
total_sales_str = f"\n**** Total Sales: ${all_costs + profit_target:.2f} ****"

recommended_selling_string = f"\n\n**** Recommended selling price: ${selling_price:.2f}"

to_write = [heading, variable_heading_txt, variable_frame_txt, variable_sub_txt,
            fixed_heading_txt, fixed_frame_txt, fixed_sub_txt,
            total_costs_str, sales_advice_txt, profit_target_txt, total_sales_str,
            recommended_selling_string]

filename = product_name

# printing area
for item in to_write:
    print(item)

# write output to file
# Create file to hold data (add .txt extension)
write_to_filename = "{}.txt".format(filename)
text_file = open(write_to_filename, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")
