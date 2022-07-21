n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
k=[]
for i in l1:
    if i not in l2:
        if i not in k:
            k.append(i)
for i in l2:
    if i not in l1:
        if i not in k:
            k.append(i)

print(*k)
