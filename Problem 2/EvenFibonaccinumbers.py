def sumfunc(n,c):
    global sum
    if c<4000000:
        x = n+c
        if(x%2 == 0):
            sum = sum+n+c
        sumfunc(c,x)
sum = 0    
fib1 = 1
fib2 = 1
sumfunc(fib1,fib2)
print(sum)
