#fibonnaci

def fib():
	a=0
	b=1
	fib=0
	print(a)
	print(b)
	for i in range(0,100):
		c=a+b
		print(c)
		a=b
		b=c
fib()
