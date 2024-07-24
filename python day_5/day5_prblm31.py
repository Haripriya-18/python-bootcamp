'''print the unquie charaters in string'''

i=input()
inp=i.lower()
vowels="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
a=" "
for i in inp:        
    if(i not in a):
        a+=i
print(a)    
        