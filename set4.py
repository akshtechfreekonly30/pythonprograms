def setfun(a,b):
    c=set()
    for i in a:
        if i not in b:
                c.add(i)
        if i not in a:
                c.add(i)
    for i in b:

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
setfun(a,bs