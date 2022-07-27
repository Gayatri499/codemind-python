n=input()
d=n.split()
k="AEIOUaeiou"
s=[]
for i in range(len(d)):
    c=0
    for j in d[i]:
        if j in k:
            c+=1
    s.append(c)
print(s.count(min(s)))
    
            
