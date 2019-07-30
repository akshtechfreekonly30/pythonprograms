def arms(a):
	b=[]
	temp=a
	while(temp>0):
		x=temp%10
		b.append(x)
		temp=temp/10
	sum=0	
	print(b)
	for i in range(0,len(b)):
		sum=sum+(b[i]*b[i]*b[i])
	print(sum)	
	if(sum==a):
		print("this is a armstrong number")
	else:
		print("this is not a armstrong number")
a=input("enter number")
arms(a)	
