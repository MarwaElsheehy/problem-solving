def multi_table(number):
    result = ""
    for i in range(1, 11):
        result += f"{i} * {number} = {i * number}\n"
    return result.strip()

print(multi_table(5))
