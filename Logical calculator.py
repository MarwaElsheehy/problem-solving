OPERATORS = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: a != b
}

def logical_calc(array, op):
    return reduce(OPERATORS[op], array)

print(logical_calc([True, False], "AND"))
