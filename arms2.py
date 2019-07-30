#armstrong in interval

def arms(a,b):
	for i in range(a,b+1):
		j=i	
		c=[]
		while(j>0):
			x=j%10
			c.append(x)
			j=j/10
		#print(c)		
		sum=0
		for x in range(0,len(c)):
			sum=sum+(c[x]*c[x]*c[x])
		#print(sum)
		if(sum==i):
			print(i)

a=input("enter a")
b=input("enter b")
arms(a,b)
