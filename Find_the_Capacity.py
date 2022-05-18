a,b,c=map(int,input().split())
cap=2*a*b*c*512
cap_kb=cap//1024
s=str(cap_kb)
print(s+"KB")