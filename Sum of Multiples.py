def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    
    res = 0
    for i in range(n, m, n):
        res += i
    return res

print(sum_mul(2, 9)) # 2 + 4 + 6 + 8 = 20
