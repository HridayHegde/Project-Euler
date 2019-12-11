import math

global factors
factors = []
def primefacts(n):

    while n%2 == 0:
        factors.append(2)
        n=n/2

    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i==0:
            factors.append(i)
            n=n/i


    if n>2:
        factors.append(n)

primefacts(600851475143)

print(max(factors))
