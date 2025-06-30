def difference_in_ages(ages):
    lowest_value = min(ages)
    highest_value = max(ages)
    diff_value = highest_value - lowest_value
    return (lowest_value, highest_value, diff_value)

print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))
