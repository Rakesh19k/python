number=input("enter the number:")
rev_string=number[::-1]
print ("reversed:",rev_string)
if number==rev_string:
	print ("number is palindrome!")
else:
	print ("number is not palindrome!")



name=input("enter the name: ")
name_rev=name[::-1]
print("reversed:",name_rev)
if name==name_rev:
	print ("name is palindrome!")
else:
	print ("name is not palindrome!")