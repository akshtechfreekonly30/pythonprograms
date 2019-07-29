#largest number in list

def large(a):
	temp=a[0]
	for i in range(len(a)):
		if(a[i]>temp):
			temp=a[i]	
	print(temp)

a=[]
ac=input("enter count of list")
for i in range(ac):
	x=input()
	a.append(x)
large(a)
