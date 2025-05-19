import re

def is_digit(n):
    x = re.fullmatch(r"\d", n)
    
    if x:
        return True
    else:
        return False

print(is_digit("a5")) # False
