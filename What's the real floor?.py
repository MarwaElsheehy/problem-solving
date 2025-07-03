def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2

print(get_real_floor(1))
print(get_real_floor(5))
print(get_real_floor(15))
