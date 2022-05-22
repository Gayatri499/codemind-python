n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
d=[0]*n
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
i=0
j=0
k=0
while i<len(e) and j<len(o):
    d[k]=e[i]
    d[k+1]=o[j]
    i+=1
    j+=1
    k+=2
while i<len(e):
    d[k]=e[i]
    k+=1
    i+=1
while j<len(o):
    d[k]=o[i]
    k+=1
    j+=1
if len(d)%2:
    d.append(0)
print(*d)