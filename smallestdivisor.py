#smallest divisor

def fun(a):
    for i in range(2,a/2+1):
        if(a%i==0):
            print(i)
            break

a=input("enter a")
fun(a)
