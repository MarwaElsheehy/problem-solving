def count_positives_sum_negatives(arr) :
    
    positive_nums = []
    sum = 0
    for num in arr :
        if num > 0 :
            positive_nums.append(num)
        elif num < 0 :
            sum += num

            
    return [len(positive_nums), sum]
            

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
