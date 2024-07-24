'''check how many vowels and consonents are  in string'''
i="hello wOrld"
inp=i.lower()
vowels="aeiou"
abc="bcdfghjklmnpqrstvwxyz"
count=0
c=0
for i in inp:
    if(i in vowels):
        count+=1
for i in inp:
    if(i in abc):
        c+=1
    #if(i not in vowels):  ---gives space
        #count+=1
        
print(count)
print(c)      