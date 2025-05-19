def string_clean(s):
    """
    Function will return the cleaned string
    """
    res = ""
    for val in s:
        if not val.isdigit():
            res += val
    return res

print(string_clean("(E3at m2e2!!)"))
