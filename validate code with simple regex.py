def validate_code(code):
    return str(code).startswith(('1', '2', '3'))

print(validate_code(123))
