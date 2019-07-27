#sum of digits

def sumdig(a):
    rem=0
    sum=0
    while a>0:
        rem=a%10
        sum=sum+rem
        a=int(a/10)
    print(sum)
    
a=input("enter a")
sumdig(a)
