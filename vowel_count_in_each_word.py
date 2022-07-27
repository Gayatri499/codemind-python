n=input()
d=n.split()
s="AEIOUaeiou"
l=[]
for i in range(len(d)):
    c=0
    for j in d[i]:
        if j in s:
            c+=1
    l.append(c)
print(*l)