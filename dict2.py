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

