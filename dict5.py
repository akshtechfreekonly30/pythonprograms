def dict(d):
    print(len(d))


d={}
i=0
str=raw_input("Enter String")
a=str.split(" ")
for i in a:
    d[i]=i
dict(d)