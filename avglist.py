#average of list


def avg(a):
    sum=0
    for i in a:
        sum=sum+i
    average=sum/(len(a))
    print(average)
a=[]
n=input("enter count of list")
for i in range(0,n):
    no=input()
    a.append(no)
avg(a)
