#vowel count


def vowelcount(a):
	count=0
	for i in range(0,len(a)):
		if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
			count+=1	
	print(count)


a=raw_input("enter string")
vowelcount(a)
