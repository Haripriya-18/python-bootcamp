#prime number is square root method
import math
n=int(input())
for i in range(2,int(math.sqrt(n))+1):
    if n%1==0:
        print("not prime number")
    else:
        print("prime number")    
    