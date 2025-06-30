def bar_triang(point_a, point_b, point_c): 
    x1 = (point_a[0] + point_b[0] + point_c[0]) / 3
    y1 = (point_a[1] + point_b[1] + point_c[1]) / 3

    return f"[{x1:.4f}, {y1:.4f}]"

print(bar_triang([4, 6], [12, 4], [10, 10]))
print(bar_triang([4, 2], [12, 2], [6, 10]))
