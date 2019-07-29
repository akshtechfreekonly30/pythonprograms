#replace blank space with /

def replace(a):
	temp=a.split(" ")
	temp2='/'
	for i in range(0,len(temp)):
		temp2=temp2+temp[i]+'/'
	print(temp2)

a=raw_input("enter string")
replace(a)
