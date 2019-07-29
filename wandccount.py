#calculate number of words and number of characters in a string

def fun(a):
	temp=a.split(" ")
	wc=0
	cc=0
	for i in temp:
		wc+=1
		for j in i:
			cc+=1
	print(wc,cc)

a=raw_input("enter string")
fun(a)
