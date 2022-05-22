n=int(input())
k=list(map(int,input().split()))
l=[]
s=n
for i in range(n//2):
    l.append(k[i])
    l.append(k[s-1])
    s-=1
if n%2:
    l.append(k[n//2])
    l.append(0)
print(*l)