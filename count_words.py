n=input().lower().split()
v="aeiou"
count=0
for i in n:
    if (i[0] in v and i[-1] not in v ):
        count+=1
print(count)