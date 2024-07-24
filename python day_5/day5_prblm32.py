#find the sum 0f numbers
s=input()
inp=s.lower()
vowels="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
check="0123456789"
sum=0
a=" "
for i in s:
    if(i in check):
        sum+=int(i)
print(sum)        
        
