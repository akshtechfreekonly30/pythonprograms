#print numbers tht are not divisible by 2 or 3 

def fun(a,b):
    for i in range(a,b+1):
        if(i%2!=0 and i%3!=0):
            print(i)

a=input("enter a")
b=input("enter b")
fun(a,b)
