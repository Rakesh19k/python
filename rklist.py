# places=["delhi","gujrat","rajsthan","punjab","bihar"]
# places_rev=reversed(places)
# for i in places_rev:
# 	places.append(i)
# 	print (i)

# number=int(input("enter the number:"))
# string=str(number)
# rev_string=string[::-1]
# print ("reversed:",rev_string)
# if string==rev_string:
# 	print ("number is palindrome")
# else:
# 	print ("numberis not palindrome")



# name=["n","i","t","i","n"]
# name_rev=name[::-1]
# print("reversed:",name_rev)
# if name==name_rev:
# 	print ("palindrome hai")
# else:
# 	print ("palindrome nahi hai")


# i=1
# while i<=4:
# 	print ("python " ,end="")
# 	j=1
# 	while j<=4:
# 		print ("rocks " ,end="")
# 		j+=1
# 	i+=1
# 	print()



# user=int(input("enter the no:"))
# n=2
# while n<=user:
# 	if user%n==0:
# 		print ("is not a prime no")
# 		break
# 	n=n+1
# else:
# 	print ("is a prime no")


# user=["Bihar","Delhi","punjab","apple", "banana", "cherry", "orange"]
# user.reverse()
# print (user)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)



# numbers=[50,40,23,70,56,12,5,90,10,7]
# max_no=numbers[0]
# for i in numbers:
# 	if i>max_no:
# 		max_no=i
# print (max_no)


# numbers=[50,40,23,70,56,12,5,90,100,10,7]
# max_no=numbers[0]
# second_max=0
# for i in numbers:
# 	if i>max_no:
# 		second_max=max_no
# 		max_no=i
# print (second_max)



# user=int(input("enter the no:"))
# user1=user
# a=1
# l=1
# while a<=3:
# 	user+=1
# 	if user%2==0:
# 		print (user)
# 		a+=1
# while l<=3:
# 	user1-=1
# 	if user1%2!=0:
# 		print (user1)
# 		l+=1



# a=[1,2,3,4,]
# a.insert(a.index(3),"BANANA")
# a[a.index(3)]='apple'
# print(a)




# user=input("enter:")
# for i in user:
# 	if i==i.upper():
# 		print (i.lower())
# 	if i==i.lower():
# 		print (i.upper())



# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# l=len(binary_number)
# s=0
# for i in range(l):
# 	s+=(binary_number[l-1-i]*(2**i))
# print(s)



# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# rev=binary_number[::-1]
# s=0
# n=0
# for i in rev:
# 	b=i*(2**n)
# 	s+=b
# 	n+=1
# print (s)

# binary_number = [0,1,0,1,0,0,1]
# rev=binary_number[::-1]
# s=0
# n=0
# c=0
# while c<len(rev):
# 	b=rev[c]*(2**n)
# 	s+=b
# 	n+=1
# 	c+=1
# print (s)





# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# print type(magic_square)
# print type(magic_square[0])
# print type(magic_square[1])

# print sum(magic_square[0])
# print sum(magic_square[1])
# print sum(magic_square[2])




# a=[]
# for i in range(10):
# 	j=input('fill the list')
# 	a.append(j)
# print(a)


	

# a=[3,2,5,7,4,1]
# a.sort()
# print (a)


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# length=len(elements)
# odd=[]
# even=[]
# for i in elements:
# 	if i%2==0:
# 		even.append(i)
# 	if i%2!=0:
# 		odd.append(i)
# print (even)
# print (odd)


# a=1
# while a<5:
# 	print (" "*(5-a)+" *"*a)
# 	a+=1

# # a=1
# # while a<5:
# # 	print ("* "*(5-a)+" "*a)
# # 	a+=1

# b=5
# a=1
# while a<b:
# 	print (" "*a+" *"*(b-a))
# 	a+=1



# print('''
#     		     *
# 	    	    ***	
# 	    	   *****
# 	    	  *******
# 	    	 *********''')




# for i in range(0,10):
# 	for i in range(0,i+1):
# 		print ("*",end=" ")
# 	print ()

# a=""
# for i in range(5):
# 	a+="* "
# 	print (a)




# L=5
# K=2*L-2
# for i in range(0,L):
# 	for j in range(0,K):
# 		print (end=" ")

# 	K=K-2
# 	for m in range(0,i+1):
# 		print ("*",end="")
# 	print () 





# user1=int(input("enter the no:"))
# user=user1
# binlist=[]
# if user==1:
# 	binlist.append(user)
# if user>1:
# 	while True:
# 		rem=user%2
# 		binlist.append(rem)
# 		div=user/2
# 		user=div
# 		if user==1:
# 			binlist.append(user)
# 			break
# finallist=binlist[::-1]
# print (finallist)








# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# max_no=0
# for i in marks:
# 	x=0
# 	for j in i:
# 		x+=j
# 	print ("year marks",x)
# 	if x>max_no:
# 		max_no=x
# print (max_no)


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# max_no=0
# l=[]
# for i in marks:
# 	x=0
# 	for j in i:
# 		x+=j
# 	l.append(x)
# 	if x>max_no:
# 		max_no=x
# print (max_no)
# print (marks[l.index(max_no)])


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# length=len(elements)
# odd=[]
# even=[]
# for i in elements:
# 	if i%2==0:
# 		even.append(i)
# 	if i%2!=0:
# 		odd.append(i)
# print (even)
# print (odd)

	

# user=int(input("enter the no:"))
# user1=user
# c=0
# x=0
# while c<3:
# 	user+=1
# 	if user%2==0:
# 		print ("even no",user)
# 		c+=1
# while x<3:
# 	user1-=1
# 	if user1%2!=0:
# 		print ("odd no",user1)
# 		x+=1






# no=112356
# nolist=[int(i) for i in str(no)]
# print (nolist)





           ####### TEST #######


# user=int(input("enter the no:"))
# count=0
# for n in range(1,user)
# 	if user%n==0:
# 		count+=n
# print (count)

# user=int(input("give"))
# a=0
# b=1
# c=0
# for i in range(user):
# 	c=a+b
# 	a=b
# 	b=c
# print (a)

# user=[4,4,5,7,8,6,41,5]
# min_=user[0]
# for i in user:
# 	if i<min_:
# 		min_=i
# print(min_)







# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# sum1=[]
# for i in n:
# 	for j in n:
# 		a=i
# 		b=j
# 		c=a+b
# 		if number==c:
# 			if [a,b] and [b,a] not in sum1:
# 				sum1.append([a,b])
# print (sum1)




# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# for i in magic_square:
# 	sum1=0
# 	for j in i:
# 		sum1+=j
# 	print (sum1)



# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# length=len(students)
# counter=0
# while counter<length:
# 	print (students[counter],(marks[counter]))
# 	counter+=1


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=[]
# even=[]
# length=0
# for i in elements:
# 	if i%2!=0:
# 		odd.append(i)
# 	if i%2==0:
# 		even.append(i)
# print (len(odd))
# print (len(even))



# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=0
# even=0
# for i in elements:
# 	if i%2!=0:
# 		odd+=i
# 	if i%2==0:
# 		even+=i
# print ("odd sum", odd)
# print ("evensum", even)


# elements = [23, 14, 56, 33, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=[]
# even=[]
# sum1=0
# sum2=0
# for i in elements:
# 	if i%2!=0:
# 		odd.append(i)
# 		sum1+=i
# 	if i%2==0:
# 		even.append(i)
# 		sum2+=i
# print (sum1)
# print (sum1/len(odd))
# print (sum2)
# print (sum2/len(even))


# elements = [23, 14, 56, 33, 12, 19, 9, 15, 25, 31, 42, 43]
# odd=[]
# even=[]
# sum1=0
# sum2=0
# total_sum=0
# for i in elements:
# 	total_sum+=i
# 	if i%2!=0:
# 		odd.append(i)
# 		sum1+=i
# 	if i%2==0:
# 		even.append(i)
# 		sum2+=i
# print ("odd",len(odd),sum1)
# print ("even",len(even),sum2)
# print ("odd",sum1/len(odd))
# print ("even",sum2/len(even))
# print ("total",total_sum,len(elements))
# print ("total",total_sum/len(elements))




# kitna_paisa_hai = [3000, 57, 44, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# crorepati=[]
# lakhpati=[]
# dilwale=[]
# for i in kitna_paisa_hai:
# 	if 10000000<(i):
# 		crorepati.append(i)
# 	if 100000<(i) and 10000000>(i):
# 		lakhpati.append(i)
# 	if 100000>i:
# 		dilwale.append(i)
# print (len(crorepati))
# print (len(lakhpati))
# print (len(dilwale))




# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# a=[]
# n=[]
# t=[]
# x=[]
# u=[]
# g=[]
# for i in char_list:
# 	if "a"==i:
# 		a.append(i)
# 	if "n"==i:
# 		n.append(i)
# 	if "t"==i:
# 		t.append(i)
# 	if "x"==i:
# 		x.append(i)
# 	if "u"==i:
# 		u.append(i)
# 	if "g"==i:
# 		g.append(i)
# print ("a",len(a))
# print ("n",len(n))
# print ("t",len(t))
# print ("x",len(x))
# print ("u",len(u))
# print ("g",len(g))


# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# a = []
# for i in n:
# 	count = 0
# 	for j in n:
# 		if i == j:
# 			count+=1
# 	if count > 1:
# 		a.append(i)
# print(a)


mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
for i in mainStr:
	if i==subStr:
		remove(i)
			print(i)
	
	

# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]

