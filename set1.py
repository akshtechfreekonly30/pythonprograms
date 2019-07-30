def setfun(a):
    count=0
    for i in a:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    print count




a=set()
str=raw_input("enter string")
for i in str:
    a.add(i)
print a
setfun(a)
