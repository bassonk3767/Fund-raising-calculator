# Imports...
import math as ma

# Functions...

# Calculates the rounded value
# of a given number as input
def round_up(amount, round_to):
    return int(ma.ceil(amount / round_to)) * round_to


# Main routine...

to_round = [2.75, 2.25, 2, 2.3454]

for item in to_round:
    rounded = round_up(item, 2)
    print(f"\n\n${item:.2f} --> ${rounded:.2f}")

