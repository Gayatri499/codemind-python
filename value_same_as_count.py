n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(n):
    if l[i]==l.count(l[i]):
        if l[i] not in c:
            c.append(l[i])
print(len(c))