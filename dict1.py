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

