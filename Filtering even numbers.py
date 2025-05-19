def kata_13_december(lst): 
    # Fix this code
    unique_list = list(dict.fromkeys(lst))
    return [i for i in unique_list if i % 2 != 0]  

print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]))
