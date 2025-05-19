def monkey_count(n):
    res = []
    while n > 0:
      res.append(n)
      n -= 1
    return res[::-1]
    

print(monkey_count(10))
