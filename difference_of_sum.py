def differenceofSum(n,m):
    add = 0
    count = 0
    for i in range(1,m+1):
        if i%n != 0:
            add += i
            
        elif i%n ==0:
            count += i
            
    return add - count
num1 = 4
num2 = 20
    
print(differenceofSum(num1, num2))
