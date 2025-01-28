"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
"""


def check_permutation(str1: str, str2: str):
    str1 = str1.lower()
    str2 = str2.lower()

    if sorted(str1) != sorted(str2):
        return False
    return True

def check_permutation2(str1: str, str2: str):
    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()
    str1_chars = {}
    str2_chars = {}

    for i in range(len(str1)):
        s1_c = str1[i]
        s2_c = str2[i]
    
        if s1_c in str1_chars:
            str1_chars[s1_c] += 1
        else:
            str1_chars[s1_c] = 1

        if s2_c in str2_chars:
            str2_chars[s2_c] += 1
        else:
            str2_chars[s2_c] = 1

    return str1_chars == str2_chars


print(check_permutation2("apple", "orange"))
print(check_permutation2("pool", "loop"))
