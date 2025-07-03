alphabet = "abcdefghijklmnopqrstuvwxyz"
def position(letter):
    return alphabet.index(letter.lower()) + 1

print(position("a"))
print(position("z"))
print(position("B"))
