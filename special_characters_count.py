n=input()
c=0
k=[0,1,2,3,4,5,6,7,8,9," "]
for i in n:
    if not(65<=ord(i)<=90) and not(97<=ord(i)<=122):
        if i not in k:
            c+=1
print(c)