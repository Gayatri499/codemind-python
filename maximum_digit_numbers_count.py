n=int(input())
l=list(map(int,input().split()))
le=[]
r=[]
for i in l:
    d=str(abs(i))
    p=len(d)
    le.append(p)
m=max(le)
for j in range(n):
    if le[j]==m and l[j] not in r:
        r.append(l[j])
print(*r)
    
    
    
    
    
        
