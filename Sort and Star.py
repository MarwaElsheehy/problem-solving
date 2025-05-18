def two_sort(arr):
    arr.sort()
    first_word = arr[0]
    result = '***'.join(first_word)
    return result
        

print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
