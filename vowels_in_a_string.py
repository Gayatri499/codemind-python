n=input()
v=input()
s=list(n)
c=0
for i in range(len(s)):
    if n[i]==v:
        print("True")
        print(i)
        c+=1
        break
if c==0:
    print("False")
        