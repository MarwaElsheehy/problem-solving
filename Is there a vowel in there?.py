vowel_char = {
  97: "a",
  101: "e",
  105: "i",
  111: "o",
  117: "u"
}

def is_vow(inp):
    result = []

    for x in inp:
        if x in vowel_char:
            result.append(vowel_char[x])
        else:
            result.append(x)
    return result


print(is_vow([100,100,116,105,117,121]))
