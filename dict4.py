def dict(a,b):
    d[1]=a
    d[2]=b
    print d

a=[]
b=[]
d={}
ac=input("enter count of 1st list")
bc=input("enter count of 2nd list")
print("enter 1st list")
for i in range(0,ac):
    a.append(input())
print "enter 2nd list"
for j in range(0,bc):
    b.append(input())

dict(a,b)