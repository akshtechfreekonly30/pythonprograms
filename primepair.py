def prime(a):                 #
    flag=0
    for i in range(2,a/2+1):
        if(a%i==0):
            flag=1
            break
    return flag

def display(list):
    count=0
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if(i!=j):
                c=prime(list[i]-list[j])
                
                if(c==0):
                    print(list[i],list[j])
                    count+=1
    print(count)


a=[]
ac=input("enter list count")
for i in range(0,ac):
    a.append(input())
display(a)
