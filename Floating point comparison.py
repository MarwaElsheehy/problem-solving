def approx_equals(a, b):
    return abs(a - b) < 0.001


print(approx_equals(175.9827, 82.25))
print(approx_equals(-156.24037, -156.24038))
print(approx_equals(123.2345, 123.234501))
