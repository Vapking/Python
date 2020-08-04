str = input("Enter A String : ")

if str.isalnum() == True :
	print(" %s is AlphaNumeric String"%(str))
elif str.isalpha() == True :
	print(" %s is Alphabet String"%(str))
elif str.isdecimal() == True :
	print(" %s is Decimal String"%(str))
elif str.isdigit() == True :
	print(" %s is Digits String"%(str))
elif str.isidentifier() == True :
	print(" %s is Identifier"%(str))
elif str.islower() == True :
	print(" %s is in Lower Order"%(str))
elif str.isnumeric() == True :
	print(" %s is Numeric String"%(str))
elif str.isprintable() == True :
	print(" %s is Printable String"%(str))
elif str.isupper() == True :
	print(" %s is in Upper Order"%(str))
elif str.isspace() == True :
	print(" %s it has Space"%(str))
elif str.istitle() == True :
	print(" %s is Title String"%(str))