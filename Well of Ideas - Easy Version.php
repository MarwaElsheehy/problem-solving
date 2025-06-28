def well(x):
    good_count = x.count("good")
    if good_count in (1, 2):
        return "Publish!"
    if good_count > 2:
        return "I smell a series!"
    else:
        return "Fail!"


print(well(['bad', 'bad', 'bad']))
print(well(['good', 'bad', 'bad', 'bad', 'bad']))
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))
