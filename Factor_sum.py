from math import sqrt
l=list(map(int,input().split(",")))
res=[]
for i in l:
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=j
    if s in l:
        res.append(i)
if len(res)==0:
    print(-1)
else:
    print(*sorted(res))
    