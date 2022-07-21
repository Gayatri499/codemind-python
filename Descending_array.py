n=int(input())
l=list(map(int,input().split()))
k=sorted(l,reverse=True)
if k==l:
    print("yes")
else:
    print("no")