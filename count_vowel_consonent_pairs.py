n=input()
d=list(n)
c=0
s="AEIOUaeiou"
e="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
p=0
n=-1
for j in range(len(d)//2):
    if (d[p] in s and d[n] in e) or (d[p] in e and d[n] in s):
            c+=1
    p+=1
    n-=1
        
print(c)