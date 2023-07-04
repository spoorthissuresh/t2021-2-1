x= int(input("Enter the value of x:"))
if x%2==0:
    x-=1
y=[]
z=-1
for i in range(x):
    z+=2
    y.append(z)
print(*y)