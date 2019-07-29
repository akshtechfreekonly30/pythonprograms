#removing nth element from a string

def removen(a,n):
	temp=[]
	for i in range(0,len(a)):	
		if(i!=n-1):
			temp.append(a[i])
		else:
			i+=1
	temp2=''
	for i in temp:
		temp2=temp2+i
	print(temp2)

a=raw_input("enter string")
n=input("enter n")
removen(a,n)
		
