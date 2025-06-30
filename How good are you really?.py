from functools import reduce
def better_than_average(class_points, your_points):
    sum_all = reduce(lambda x, y: x +  y, class_points)
    
    if sum_all / len(class_points) < your_points :
        return True
    else:
        return False
    

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
