#check given year a leap year or not


def leap(a):
	if(a%4==0):
		if(a%100==0):
			if(a%400):
				print("this is a leap year")
			else:
				print("this is not a leap year")

		else:
			print("this is a leap year")
	else:
		print("this is not a leap year")
a=input("enter year")
leap(a)
