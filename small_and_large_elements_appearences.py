n=list(input())
k=[]
for i in n:
    if i==" ":
        n.remove(i)
k.append(min(n))
k.append(n.count(min(n)))
k.append(max(n))
k.append(n.count(max(n)))
print(*k)
