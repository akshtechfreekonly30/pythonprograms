#merging and sorting 2 lists

def fun(a,b):
	c=[]	
	for i in range(len(a)):
		c.append(a[i])
	for j in range(len(b)):
		c.append(b[i])
	c.sort()	
	for i in range(len(c)):
		print(i)

ac=input("enter count of 1st list")
a=[]
for i in range(ac):
	x=input()
	a.append(x)
b=[]
bc=input("enter count of 2nd list")
for i in range(bc):
	x=input()
	b.append(x)
fun(a,b)
