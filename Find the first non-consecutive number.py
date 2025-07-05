def first_non_consecutive(arr):
    if len(arr) < 2:
        return None

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    
    return None

print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))  
print(first_non_consecutive([1, 2, 3, 4, 5]))        
print(first_non_consecutive([-3, -2, -1, 0, 2]))     
print(first_non_consecutive([7]))                    
print(first_non_consecutive([])) 
