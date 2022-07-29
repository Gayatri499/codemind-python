n=input().split()
k=[]
for i in n:
    k.append(min(i))
    k.append(max(i))
print(*k)
