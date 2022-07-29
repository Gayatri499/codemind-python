n=input().split()
mn=0
mx=0
for i in n:
    mn=ord(min(i))
    mx=ord(max(i))
    print(abs(mx-mn),end=" ")
    mn=0
    mx=0