#grade

def grade(a):
    total=0
    for i in a:
        total=total+i
    print(total)
    per=float(total/5)
    print(per)
    if per>80:
        print("a")

    elif per>70:
        print("b")

    elif per>60:
        print("c")

    elif per>50:
        print("d")

    elif per>40:
        print("e")

    else:
        print("fail")

print("enter marks of 5 subjects")
a=[]
for i in range(0,5):
    inp=input()
    a.append(inp)
print(a)
grade(a)
