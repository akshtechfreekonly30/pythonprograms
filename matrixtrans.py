a=[[1,2,3],[3,2,1]]
b=[[0,0],[0,0],[0,0]]
for i in range(len(a)):
	for j in range(len(b)):
		b[j][i]=a[i][j]
print(a)
print(b)
