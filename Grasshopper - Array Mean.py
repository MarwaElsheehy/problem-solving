def find_average(nums):
    
    res = reduce(lambda x, y: x + y, nums)
    return ceil(res / len(nums))
    

print(find_average([1, 3, 5, 7]))
print(find_average([1]))
