def to_alternating_case(string):
    return "".join([c.swapcase() for c in string])

print(to_alternating_case("HeLLo WoRLD"))
print(to_alternating_case("hello WORLD"))
print(to_alternating_case("1a2b3c4d5e"))
