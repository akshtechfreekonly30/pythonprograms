#counting number of digits

def countdig(a):
    i=0
    while a>=1:
        i+=1
        a=int(a/10)
    print(i)

a=input("enter a")
countdig(a)
