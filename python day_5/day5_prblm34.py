'''find ascii values by range'''
#for i in range(32,128):
 #   print(chr(i),end=" ")

'''converting the integer into ascii value and find sum for values'''
#s=input()
#sum=0
#for i in s:
   # if(ord(i)>=48 and ord(i)<=57):
   #     sum+=int(i)
#print(sum)


'''converting the integer into ascii value and find sum for ascii values'''
#s="hello 123"
#c="0123456789"
#sum=0
#for i in s:
 #   if(i in c):
  #      sum+=ord(i)
#print(sum)  o/p is 150

'''write a code to print all the capital letters in a given string'''

#for i in range(65,90):
 #   print(chr(i),end=" ")


'''remove all the brackets from the algberic expression'''
#s=input()
#for i in s:
    #if(i!=chr(40) and i!=chr(41) and i!=chr(91) and i!=chr(93) and i!=chr(123) and i!=chr(125) ):
 #   if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
  #      pass
   # else:
    #    print(i,end=" ")
#print()        

'''print EFG example-ABC,4'''
#s=input()
#n=int(input())
#for i in s:
 #   e=ord(i)+n
  #  print(chr(e),end="")



'''INPUT-> hello-----wor---ld  output-> ------helloworld'''
#print("--"*30) o/p-------------
s="hello----wor--ld"
new=" "
count=0
for i in s:
    if(i=="-"):
        count+=1
    else:
        new+=i
print("-"*count+new,end=" ")






