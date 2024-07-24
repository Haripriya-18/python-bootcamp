# GCD (greatest common divider)
#GCD of two numbers
#using EDCLIDIAN ALGROITHM
a=int(input())
b=int(input())


while b!=0:
    a,b=b,a%b



    a,b=b,(a*b)//a
    s=a
print(s)
