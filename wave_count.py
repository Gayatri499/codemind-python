n=int(input())
k=list(map(int,input().split()))
c=0
if n%2==0:
    for i in range(1,n-1,2):
        if (k[i-1]<k[i]>k[i+1]):
            c+=1
        else:
            c=0
            break
if n%2!=0:
    for i in range(1,n,2):
        if (k[i-1]<k[i]>k[i+1]):
            c+=1
        else:
            c=0
            break
if c==0:
    print(-1)
else:
    print(c)