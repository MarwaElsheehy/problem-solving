def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * (discount / 100))

print(duty_free(12, 50, 1000))
