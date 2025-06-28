def flip(text, arr):
    return sorted(arr) if text == 'R' else sorted(arr, reverse=True)

print(flip('R', [3, 2, 1, 2]))
print(flip('L', [1, 4, 5, 3, 5]))
