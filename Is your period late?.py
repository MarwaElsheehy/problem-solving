from datetime import date
def period_is_late(last,today,cycle_length):

    return (today - last).days > cycle_length

print(period_is_late(date(2023, 5, 1), date(2023, 5, 30), 28))  
