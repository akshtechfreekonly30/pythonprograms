<<<<<<< HEAD
def dict(d):
    sum=0
    for i in range(0,len(d)):
        sum=sum+d[i]
    print(d)
    print sum

dc=input("enter count")
print "enter elements"
d={}
for i in range(0,dc):
    d[i]=input()
dict(d)

=======
#concatinating two dictionaries

dict1={
	0:'pooja',
	1:'akshay',
	2:'sonu'
}

dict2={
	3:'bhandare',
	4:'gaju',
	5:'aarti'
}

dict1.update(dict2)
print(dict1)
>>>>>>> 50f6d8708148bb96b3e86814fd1924485b26c469
