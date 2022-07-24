d=input()
l=d.split()
m=0
for i in l:
    s=len(i)
    if s>m:
        m=s
print(m)