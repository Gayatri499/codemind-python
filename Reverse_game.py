i=int(input())
l=list(map(int,input().split()))
rev=[]
for n in l:
    s=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    rev.append(s)
        
print(*rev)