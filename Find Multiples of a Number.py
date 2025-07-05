def find_multiples(integer, limit):
  return list(range(integer, limit + 1, integer))

print(find_multiples(5, 25))
print(find_multiples(1, 2))
