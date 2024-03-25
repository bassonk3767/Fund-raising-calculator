# Imports...


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


# Main routine...
get_int = num_check("\nHow many do you need?\n~~~ ",
                    "\nPlease enter an amount more than 0\n",
                    int)
