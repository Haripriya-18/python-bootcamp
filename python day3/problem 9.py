#find the sum of elements that is present in k+ith index k is given by user
#k=3
#n=2
#input:3 6 8 61 2
#output=2
#k=3
#n=4
#input=70 54 36 72
#output=error0
n=int(input())
k=int(input())
list=list(map(int,input().split(" ")))
if(len(list)<k+n):
    print("ERROR")
else:    
    for i in range(0,len(list)):
        print(list[k+n])
        break
 #print the element in a particular index5       

  
