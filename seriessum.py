#find sum of series till n

def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)

n=input("enter n")
sum(n)
