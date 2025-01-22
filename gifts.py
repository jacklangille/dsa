# """ Build a function that will randomly assign gifts between people in different families.
# At the end everybody must have a gift and someone's gift can't come from a member of the same family.
# We start with 5 people A1,A2,B1,B2,C1. You are free to define the function input data structure, output
# must be a map of giver:giftee
# Example Solution A1:B1 A2:C1 B1:A1 B2:A2 C1:B2
# family_input = [”A1”, “A2”, “B1”, “B2”, “C1”]


# Solution
# Input: List
# Output: Map
# Gifts cant be from the same family i.e. assignments["A_"][0] != A

from typing import List, Dict


def assign_gifts(members: List[str]) -> Dict[str, str]:

    assignments = {}

    for giver in members:
        family = giver[0]

        # Find the first valid recipient not in the same family
        for recipient in members:
            if recipient[0] != family and recipient not in assignments.values():
                assignments[giver] = recipient
                members.remove(recipient)
                break
        else:
            # If no valid recipient is found, restart the process
            return assign_gifts(members)

    return assignments


family_input = ["A1", "A2", "B1", "B2", "C1"]
output = assign_gifts(family_input)
print(output)
