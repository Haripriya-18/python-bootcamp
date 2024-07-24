#print the element in a particular index
#70 54 36 72 76 9999 0089
#1   2  3  4  5  6    7
#k=20,len=7
#index=6
list=list(map(int,input().split( )))
k=int(input())
for i in range(len(list)):
    print(k%len(list))
    break


