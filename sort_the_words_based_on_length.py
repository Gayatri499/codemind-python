n=input().split()
n.sort()
print(*sorted(n,key=len))
