def setfun(a,b):
    c=set()
    for i in a:
        if i in b:
                c.add(i)
    print c

a=set()
b=set()
str1=raw_input("enter 1st string")
str2=raw_input("enter 2nd string")
for i in str1:
    a.add(i)
for j in str2:
    b.add(j)
print a,b
setfun(a,b)