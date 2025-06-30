def evil(n):
    binary_ones = bin(n).count("1")
    if binary_ones % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
    
print(evil(1))
print(evil(2))
print(evil(3))
