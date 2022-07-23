i=int(input())
l=list(map(int,input().split()))
s=0
c=0
for n in l:
    temp=n
    s=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    if s==temp:
        c+=1
        
print(c)