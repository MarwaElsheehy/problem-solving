import math
def square_or_square_root(arr):
    return [int(math.sqrt(x)) if math.sqrt(x).is_integer() else x ** 2 for x in arr]


print(square_or_square_root([4,3,9,7,2,1]))
