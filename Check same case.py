def same_case(a, b): 
    if a.islower() and b.islower():
      return 1
    elif a.isupper() and b.isupper():
      return 1
    elif not a.isalpha() or not b.isalpha():
      return -1
    else:
      return 0

print(same_case('C', 'B'))
print(same_case('\t', 'Z'))
print(same_case('A', 's'))
