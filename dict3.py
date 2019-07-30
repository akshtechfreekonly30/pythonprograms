def dict(d,key):
    if key in d:
        del d[key]
    print d
dc=input("enter count")
print "enter elements"
d={}
for i in range(0,dc):
    a=input("Enter key")
    b=raw_input("Enter value")
    d[a]=b
key=input("enter key to be deleted")
dict(d,key)

