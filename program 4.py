x = [1,2,3,4,5,6,7,8,9] 
y = map(int,input().split())
y = list(y)
z= {} 
for a in x:
    count = 0
    for b in y:
        if(b%a)==0:
            count=count+1
        else:
            pass
        z.update({a:count})
print(z)
