'''reverse the string'''
s=input()
check="0123456789"
ans=""
for i in s:
    if(i in check):
        ans+=i
ans=int(ans)        
print(ans)
while(ans>0):
    r=ans%10
    ans=ans//10
    print(r,end="")    
