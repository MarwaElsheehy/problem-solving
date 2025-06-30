def none(lst, func):
    return not any(func(x) for x in lst)

print(none([], lambda x: x > 0))
