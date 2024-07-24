#prime number using half iteration method
n=int(input())
if(n>1):
    for i in range(2,int(n/2)+1):
        if n%1==0:
            print("number is not prime")
            break
        else:
            print("prime number")
else:
    print("number is not prime")
                
            