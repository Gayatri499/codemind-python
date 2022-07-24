d=input()
l=d.split()
le=[]
for i in range(len(l)):
    if i%2==0:
        le.append(l[i][::-1])
    else:
        le.append(l[i])
print(" ".join(le))
        