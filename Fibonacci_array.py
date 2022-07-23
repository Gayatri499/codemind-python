n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(0,n-2):
    if k[i+2]==k[i]+k[i+1]:
        c+=1
    else:
        c=0
        break
if c==0:
    print("no")
else:
    print("yes")