<<<<<<< HEAD
def dict(d):
    mul=1
    for i in range(0,len(d)):
        mul=mul*d[i]
    print(d)
    print mul

dc=input("enter count")
print "enter elements"
d={}
for i in range(0,dc):
    d[i]=input()
dict(d)

=======
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
>>>>>>> 50f6d8708148bb96b3e86814fd1924485b26c469
