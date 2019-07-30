#anagram array

def annagram(a,b):
	flag=0
	for i in a:
		if i not in b:
			flag=1 
	if(flag==0):
		print("strings are annagram")
	else:
		print("strings are not annagram")

a=raw_input("enter 1st string")
b=raw_input("enter 2nd string")
annagram(a,b)
