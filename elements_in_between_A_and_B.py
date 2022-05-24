n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in k:
    if a<=i<=b:
        c+=1
        print(i,end=" ")
if c==0:
    print(-1)