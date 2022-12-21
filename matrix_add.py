a=[[2,4],[5,3]]
b=[[4,7],[6,1]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        c[i][j]=a[i][j]+b[i][j]
print(c)