n=int(input())
k=list(map(int,input().split()))
l=[]
s=0
for i in range(n//2):
    l.append(k[s])
    l.append(k[s+1])
    s+=2
if n%2:
    l.append(k[-1])
    l.append(0)
print(*l)