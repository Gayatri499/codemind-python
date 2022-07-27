n=input()
s="AEIOU"
u="aeiou"
cc=0
sc=0
for i in s:
    if i in n:
        cc+=1
    else:
        cc=0
        break
for i in u:
    if i in n:
        sc+=1
    else:
        sc=0
        break
if cc!=0 or sc!=0:
    print("True")
else:
    print("False")