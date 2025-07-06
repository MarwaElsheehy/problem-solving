def triple_trouble(one, two, three):
    result = ""
    for i in range(len(one)):
        result += one[i] + two[i] + three[i]
    return result

print(triple_trouble("aaa","bbb","ccc"))
print(triple_trouble("Bm", "aa", "tn"))
print(triple_trouble("LLh", "euo", "xtr"))
