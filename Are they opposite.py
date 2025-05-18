def is_opposite(s1, s2):
    if not s1 or not s2:
        return False
    elif s1.lower() == s2.lower() and s1 != s2:
        return True


print(is_opposite("ab", "AB"))
print(is_opposite("aBcd","AbCD"))
print(is_opposite("AB","Ab"))
