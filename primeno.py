#prime number

def prime(a):
	c=0
	for i in range(2,(a/2+1)):
		if(a%i==0):
			c=1
			break
	if(c==0):
		print("this is a prime number")
	else:
		print("this is not a prime number")

a=input("enter number")
prime(a)
