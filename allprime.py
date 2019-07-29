def allprime():
	for a in range(0,101):
		c=0
		for i in range(2,(a/2+1)):
			if(a%i==0):
				c=1
				break
		if(c==0):
			print(a)


allprime()
