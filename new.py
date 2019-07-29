str=raw_input("Enter String: ")




list=str.split(" ")
print(list)
list2=[]
for i in range(len(list)):
	
	for j in range(i+1,len(list)):
		if(list[i]>list[j]):
			temp=list[i]
			list[i]=list[j]
			list[j]=temp

#for i in range(len(str)):
#	list.append(str[i])
#for i in range(len(list)):
#	for
print(list)
