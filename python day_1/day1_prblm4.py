#palindrome
num=int(input())
reverse=0
i=num
while(num>0):
    reverse=reverse*10+num%10
    num=num//10
if(i==reverse):
    print("it is a polindrome")
else:
    print("it is not polindrome")      