from math import sqrt
def prime(i):
    if i==1 or i==0:
        return False
    s=int(sqrt(i))
    for j in range(2,s+1):
        if i%j==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if prime(i):
        c+=1
print(c)