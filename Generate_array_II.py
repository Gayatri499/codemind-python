n=int(input())
k=list(map(int,input().split()))
l=[]
for i in range(0,n,2):
    for j in range(k[i+1]):
        l.append(k[i])
print(*l)