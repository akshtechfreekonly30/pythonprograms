#print all numbers divisible by given number

def div(a):
    for i in range(1,100):
        if(i%a==0):
            print(i)

a=input("enter number")
div(a)
