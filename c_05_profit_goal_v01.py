# Imports

# Functions

# Main routine


# RECYCLED FUNCTION

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


# Finds the profit goal
def profit_goal(total_costs):
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
            amount = response[-1]

        else:
#  response for now            profit_type = "unknown"
