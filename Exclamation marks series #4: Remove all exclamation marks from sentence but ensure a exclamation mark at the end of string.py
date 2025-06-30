def remove(st):
    st = st.replace("!", "")
    return st + "!" 

print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("!Hi!"))
print(remove("!Hi"))
print(remove("Hi"))
