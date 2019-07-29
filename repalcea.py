#replacing a with $

def replace(strg):
	temp=[]
	temp2=''
	for i in strg:
		temp.append(i)
	
	for i in range(0,len(temp)):
		if(temp[i]=='a'):
			temp[i]='$'
	for i in temp:
		temp2=temp2+i
	print(temp2)
strg=raw_input("enter string")
replace(strg)
