n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(n):
    if not(a<=l[i]<=b):
        s+=l[i]
print(s)
        