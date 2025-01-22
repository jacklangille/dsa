def is_valid(s: str) -> bool:
    pairs = {"(": ")", "{": "}", "[": "]"}
    stack = []
    
    for c in s:
        if c in pairs:  # If it's an opening bracket
            stack.append(pairs[c])
        elif not stack or stack.pop() != c:  # If it's a closing bracket
            return False
    
    return True if not stack else False




s1 = "()[]{}" # Valid
s2 = "([{(}])" # Invalid
print(is_valid((s1)))

print(is_valid((s2)))
