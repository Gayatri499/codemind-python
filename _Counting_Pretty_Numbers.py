t=int(input())
for i in range(t):
    c=0
    l,r=map(int,input().split())
    for j in range(l,r+1):
        if str(j)[-1]=="2" or str(j)[-1]=="3" or str(j)[-1]=="9":
            c+=1
    print(c)
            
    
    