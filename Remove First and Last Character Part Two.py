def array(string):
    parts = string.split(',')
    print(parts)
    if len(parts) <= 2:
        return None
    return ' '.join(parts[1:-1])

print(array('1,2,3,4'))
