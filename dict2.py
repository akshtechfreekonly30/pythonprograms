#checking if key is in dictionary

def checkkey(dict1,key):
	flag=0
	if key not in dict1:
		flag=1
	if(flag==0):
		print("key is present in dictionary")
	else:
		print("key is not present in dictionary")

dict1={
	1:'pooja',
	2:'aarti',
	3:'akshay'
}
key=input("enter key to be searched")
checkkey(dict1,key)
