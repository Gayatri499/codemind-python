n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=max(l)
if not(a<=c<=b):
    print(c)
else:
    print(-1)