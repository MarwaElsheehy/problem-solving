import re
def remove(st):
    cleaned_text = re.sub(r'!+$', '', st)
    return cleaned_text
    
print(remove("!Hi!!!"))
