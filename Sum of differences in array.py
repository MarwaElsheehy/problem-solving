def sum_of_differences(arr):
    
    arr.sort(reverse=True)
    return sum(arr[i] - arr[i + 1] for i in range(len(arr) - 1))

print(sum_of_differences([1, 2, 10]))
