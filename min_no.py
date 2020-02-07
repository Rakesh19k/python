def min(user):
	min_no=user[0]
	for i in user:
		if i < min_no:
			min_no=i
	return min_no
user=input("enter the number: ").split()
print (min(user))