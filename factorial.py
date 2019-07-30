#factorial

def fact(a):
	fact=1
	for i in range(a,0,-1):
		fact=fact*i
	print(fact)

a=input("enter number")
fact(a)
