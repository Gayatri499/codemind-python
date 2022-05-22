n=int(input())
k=list(map(int,input().split()))
c=0
l=[]
for i in k:
    if i%2:
        if i not in l:
            l.append(i)
            c+=1        
print(c)