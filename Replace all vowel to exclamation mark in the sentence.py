def replace_exclamation(st):

    return "".join(["!" if s in "aeiouAEIOU" else s for s in st])

print(replace_exclamation("aeiou"))
print(replace_exclamation("Hi!"))
