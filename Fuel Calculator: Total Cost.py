def fuelPrice(litres, pricePerLiter):
    discount = min(litres // 2, 5) * .05
    return round(litres * (pricePerLiter - discount), 2)

print(fuelPrice(10, 21.5))
