def generate_range(start, stop, step):
    result = []
    while start <= stop:
        result.append(start)
        start += step
    return result

print(generate_range(1, 10, 1))
print(generate_range(-10, 1, 1))
print(generate_range(1, 15, 20))


def generate_range(start, stop, step):
    
    return [i for i in range(start, stop + 1, step)]

print(generate_range(1, 10, 1))
print(generate_range(-10, 1, 1))
print(generate_range(1, 15, 20))
