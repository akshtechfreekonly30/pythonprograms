#printing all possible combinations of digits

a=input("enter a")
b=input("enter b")
c=input("enter c")
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j and j!=k and k!=i):
                print(d[i],d[j],d[k])
