#palindrome string


def palindrome(a):
	c=0
	j=len(a)-1
	for i in range(0,(len(a)-1)):
		if(a[i]!=a[j]):
			c=1
			break
		j-=1	
	print(c)
	if(c==0):
		print("string is palindrome")
	else:
		print("string is not plaindrome")

a=raw_input("enter string")
palindrome(a)
