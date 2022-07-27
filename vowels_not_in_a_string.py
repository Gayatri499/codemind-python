n=input()
k="aeiou"
d=[]
for i in k:
    if i not in n:
        d.append(i)
s=sorted(d)
if len(d)!=0:
    print(" ".join(s))
else:
    print(0)
        
