s=int(input())
l=list(map(int,input().split()))
rev=[]
for n in l:
    i=0
    while n:
        r=n%10
        i+=1
        n=n//10
    rev.append(i)
        
print(rev.count(min(rev)))