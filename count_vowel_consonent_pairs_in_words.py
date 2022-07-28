n=input().split()
c=0
s="AEIOUaeiou"
for i in n:
    p=0
    n=-1
    for j in range(len(i)//2):
        if (i[p] in s and i[n] not in s) or (i[p] not in s and i[n] in s):
            c+=1
        p+=1
        n-=1
        
print(c)