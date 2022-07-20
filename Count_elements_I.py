n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=set(a)
e=set(b)
for i in d:
    if i in e:
        c+=1
print(c)