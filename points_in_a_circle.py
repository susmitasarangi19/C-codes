count=0
a=[3,3,2]
b=[5,3,2]
if(a[0]<b[0]):
    x1=list(range(a[0],b[0]+1))
else:
    x1=list(range(b[0],a[0]+1))
    
    
if(a[1]<b[1]):
    y1=list(range(a[1],b[1]+1))
else:
    y1=list(range(b[1],a[1]+1))
print(x1)
print(y1)
for x in x1:
    for y in y1:
        if(((a[0]-x)*(a[0]-x))+((a[1]-y)*(a[1]-y))<=a[2]*a[2] and (b[0]-x)*(b[0]-x)+(b[1]-y)*(b[1]-y)<=b[2]*b[2]):
            count+=1
print(count)