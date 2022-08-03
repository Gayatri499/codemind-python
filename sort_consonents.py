n=input().split()
l1=[]
s="aeiou"
for i in n:
    k=[]
    for j in i:
        if j not in s:
            k.append(j)
    k=sorted(k)
    i=list(i)
    p=0
    for x in range(len(i)):
        if i[x] not in s:
            i[x]=k[p]
            p+=1
    l1.append("".join(i))
    k.clear()
print(*l1)