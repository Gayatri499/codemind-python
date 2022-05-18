n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]==0 or l[i]==1:
        c+=1
    else:
        c=0
        break
if c==0:
    print("False")
else:
    print("True")