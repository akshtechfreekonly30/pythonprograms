#second largest in list

def seclarge(a):
	'''for i in range(0,len(a)):
		for j in range(1,i):
			if(a[i]>a[j]):
				temp=a[i]
				a[i]=a[j]
				a[j]=temp'''	
	a.sort()
	print(a)
	print(a[len(a)-2])

a=[]
ac=input("enter count of array")
print("enter array")
for i in range(ac):
	x=input()
	a.append(x)
seclarge(a)
