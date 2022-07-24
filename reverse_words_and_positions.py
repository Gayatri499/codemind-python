d=input()
l=d.split()
le=[]
for i in range(len(l)):
        le.append(l[i][::-1])
print(" ".join(le[::-1]))