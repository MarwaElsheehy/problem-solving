def correct_polish_letters(st):
    pol = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}

    final = ""
    for val in st:
        if val in pol:
           final += pol[val]
        else:
           final += val
    return final

print(correct_polish_letters("Jędrzej Błądziński"))
