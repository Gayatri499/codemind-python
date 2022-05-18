n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(n):
    if l[i]==l.count(l[i]):
        if l[i] not in c:
            c.append(l[i])
if len(c)==0:
    print(-1)
else:
    print(*c)