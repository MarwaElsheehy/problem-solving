def draw_stairs(n):
    result = ""
    for i in range(n):
        result += " " * i + "I"
        if i != n - 1:
            result += "\n"
    return result


print(draw_stairs(3))
