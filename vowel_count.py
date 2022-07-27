n=input()
k="AEIOUaeiou"
c=0
for i in n:
    if i in k:
        c+=1
if c==0:
    print(0)
else:
    print(c)
    