def exc():
    a=10
    b=0
    try:
        c=a/b
    except(ZeroDivisionError ):
        print("Divide by zero")
exc()
