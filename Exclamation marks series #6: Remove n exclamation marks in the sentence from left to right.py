def remove(s, n):
    result = []
    for char in s:
        if char == '!' and n > 0:
            n -= 1
        else:
            result.append(char)
    return ''.join(result)

print(remove("!!!Hi !!hi!!! !hi", 5))

def remove(s, n):
    return s.replace('!', '', n)

print(remove("!!!Hi !!hi!!! !hi", 5))
