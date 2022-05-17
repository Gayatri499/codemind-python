n=int(input())
l=list(map(int,input().split()))
c=l.copy()
k=0
count=0
for j in range(2):
    c.append(l[j])
for i in range(n):
    if (c[k]%2!=0 and c[k+2]%2==0) or (c[k]%2==0 and c[k+2]%2!=0):
        count+=1
    k+=1
print(count)