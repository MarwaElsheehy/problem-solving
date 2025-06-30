def lowercase_count(strng):
    res = []
    for s in strng:
        if s.islower():
            res.append(s)
    return len(res)

print(lowercase_count("abcABC123"))
