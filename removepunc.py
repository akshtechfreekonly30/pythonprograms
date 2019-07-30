#removing punctuations from a string

def rempunc(a):
	punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	not_punc=''
	for i in a:
		if i not in punc:
			not_punc=not_punc+i
	print(not_punc)
a=raw_input("enter string")
rempunc(a)
