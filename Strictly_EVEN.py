n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]%2:
        continue
    if i%2==0 and l[i]%2==0:
        c+=1
    elif i%2!=0 and l[i]%2==0:
        c=0
        print("False")
        break
if c!=0:
    print("True")