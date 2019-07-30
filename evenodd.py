#seprating even odd

def evenodd(a):
	even=[]
	odd=[]
	for i in range(len(a)):
		if(a[i]%2==0):
			even.append(a[i])
		if(a[i]%2==1):
			odd.append(a[i])
	print(odd,even)
ac=input("enter count of list")
a=[]
for i in range(ac):
	a.append(input())
evenodd(a)
