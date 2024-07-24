# prime number in traditional/square root method
a=int(input())
r=a**0.5
count=0
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break
if count==0:
    print("prime number")
else:
    print("not prime number")

# write a program to print all the prime number in a given range
a=int(input())
b=int(input())
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end="")
