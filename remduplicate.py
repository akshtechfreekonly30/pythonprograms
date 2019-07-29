#deleting duplicate elements from lists

def delete(a):
	temp=[]
	for i in range(0,len(a)):
		if a[i] not in temp:
			temp.append(a[i])	
	print(temp)

a=[]
ac=input("enter count of array")
for i in range(0,ac):
	a.append(input())
delete(a)
