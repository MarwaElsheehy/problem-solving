def get_drink_by_profession(param):
    drinks = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    return drinks.get(param.lower(), "Beer")


print(get_drink_by_profession("pOLitiCIaN"))  
print(get_drink_by_profession("Jabroni"))     
print(get_drink_by_profession("Doctor")) 
