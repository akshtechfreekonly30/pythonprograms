g=raw_input("enterr gender M/F")
sal=input("enterv salary")
if(g=='m'):
    if(sal>250000):
        print("tax applicable for male")
    else:print("tax not applicable for male")

else:
    if(sal>300000):
        print("tax applicable for female")
    else:print("tax not applicable for female")
