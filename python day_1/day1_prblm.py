#find the amstrong number
n=int(input())
s=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+r**b
    n=n//10
if s==sum1:
    print("amstrong number") 
else:
    print("not amstrong number")       