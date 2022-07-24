n=int(input())
l=list(map(int,input().split()))
le=[]
for i in l:
    d=str(abs(i))
    p=len(d)
    le.append(p)
print(*le)
