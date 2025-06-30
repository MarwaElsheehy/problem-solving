def find_slope(points):
    while True:
        try:
            m = (points[3] - points[1]) // (points[2] - points[0])
        except ZeroDivisionError:
            return 'undefined'
        else:
            return str(m)
            
            
print(find_slope([19,3,20,3]),"0")
print(find_slope([-7,2,-7,4]),"undefined")
