def solution(a, b):
    if len(a) < len(b):
        return a + b + a 
    else:
        return b + a + b
    
print(solution('45', '1'))
print(solution('13', '200'))
print(solution('1', '22'))
