from numpy import prod
def find_difference(a, b):
    return abs(prod(a) - prod(b))
    

print(find_difference([3, 2, 5], [1, 4, 4]))
