#printing even numbers

def oddno(a,b):
    for i in range(a,b+1):
        if(i%2==1):
            print(i)

a=input("enter a")
b=input("enter b")
oddno(a,b)
