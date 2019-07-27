#palindrome

def palindrome(a):
    rev=0
    rem=0
    temp=a
    while a>0:
        rem=a%10
        rev=(rev*10)+rem
        a=a//10
    print(rev)
    if(rev==temp):
        print("a is palindrome")
    else:
        print("a is not palindrome")

a=input("enter a")
palindrome(a)
