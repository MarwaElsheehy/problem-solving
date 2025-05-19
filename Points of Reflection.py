def symmetric_point(p, q):
    x = 2 * q[0] - p[0]
    y = 2 * q[1] - p[1]
    return [x, y]

print(symmetric_point([1, 2], [2, 3]))
