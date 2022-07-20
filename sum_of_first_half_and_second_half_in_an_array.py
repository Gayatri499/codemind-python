n=int(input())
l=list(map(int,input().split()))
f=[]
s=[]
if len(l)%2==0:
    k=len(l)//2
    for i in range(k):
        f.append(l[i])
    for j in range(i+1,len(l)):
        s.append(l[j])
    print(sum(f))
    print(sum(s))
else:
    k=len(l)//2
    for i in range(k):
        f.append(l[i])
    for j in range(i+1,len(l)):
        s.append(l[j])
    print(sum(f))
    print(sum(s))