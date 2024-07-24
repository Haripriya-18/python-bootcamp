'''print all the vowels followed by consonent'''
i="hello world"
inp=i.lower()
vowels="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
ans=" "
a=" "
for i in inp:
    if(i in vowels):
        ans+=i
for i in inp:        
    if(i in abc):
        a+=i
print(ans)    
        