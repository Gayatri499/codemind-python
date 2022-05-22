n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    if i%2==0:
        if i not in l:
            l.append(i)
print(sum(l))