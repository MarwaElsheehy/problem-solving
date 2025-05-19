import heapq
def two_highest(arg1):
    
    new_list = set(arg1)

    highest_value1 = heapq.nlargest(2, new_list)
    return highest_value1

print(two_highest([4, 10, 10, 9]))
