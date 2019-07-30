a=[[1,2,3],[3,2,1]]
b=[[3,2,1],[1,2,3]]
c=[[0,0,0],[0,0,0]]
for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(b)):
			c[i][j]=a[i][k]*b[k][j]
print(a,b,c)
