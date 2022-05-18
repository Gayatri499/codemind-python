n=int(input())
k=list(map(int,input().split()))
c=[]
for i in k:
    if i not in c:
        c.append(i)
print(*c)