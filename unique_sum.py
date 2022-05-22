n=int(input())
k=list(map(int,input().split()))
s=0
l=[]
for i in k:
    if i not in l:
        l.append(i)
print(sum(l))