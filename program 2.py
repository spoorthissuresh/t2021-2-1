x=int(input())
l=[]
for i in range(1,x+1):
    sum=i*(i-1)
    l.append(sum)
print(*l)