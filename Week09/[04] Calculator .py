def calculator(n) :
    if n <= 1 :
        return n
    
    result = 0
    k = len(str(n))

    for i in range(1,k+1) :
        min_point = 10**(i-1)
        max_point = min(n, 10**i - 1)

        result += (max_point - min_point + 1) * i
    
    return result + n

print(calculator(int(input())))