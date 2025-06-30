def add_extra(list_of_numbers):
    
    new_list = list_of_numbers[:] # Make a shallow copy of the original list
    new_list.append(13)      
    return new_list

print(add_extra([1, 2, 3, 13])) 
