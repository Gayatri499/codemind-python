n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=[]
for i in range(n):
    if l.count(l[i])==k:
        if l[i] not in c:
            c.append(l[i])
if len(c)==0:
    print(-1)
else:
    print(*c)