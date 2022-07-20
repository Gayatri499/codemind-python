n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=set(a)
e=set(b)
for i in d:
    if i not in e:
        c+=1
for i in e:
    if i not in d:
        c+=1
print(c)