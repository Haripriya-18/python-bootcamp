#Replace the elements in the array with average of maximum and minimum elements in an array
#test case:0
#13 2 67 20 68
#maximum=68
#minimum=2
#68+2=70
#average=35
list=list(map(int, input().split( )))
max=list[0]
min=list[0]
n=len(list)
newlist=[]
for i in range(n):
    if(list[i]>max):
      max=list[i]
for i in range(len(list)):
    if(list[i]<min):
      min=list[i]
    sum=min+max
a=sum//2
for i in range(n):
    print(a,end=" ")           