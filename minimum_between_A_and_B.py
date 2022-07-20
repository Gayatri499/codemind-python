n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in k:
    if i>=a and i<=b:
        l.append(i)
if len(l)!=0:
    print(min(l))
else:
    print(-1)
