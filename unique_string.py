"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def check_string(input: str)->bool:

    input = input.lower()
    chars = []
    
    for c in input:
        if c in chars:
            return False
        else:
            chars.append(c)
    return True

def check_string2(input: str)->bool:
    input = input.lower()

    for i in range(len(input)):
        if input[i] in input[i+1:]:
            return False
    return True



print(check_string2("hello"))
print(check_string2("Help"))
print(check_string2("Health"))
