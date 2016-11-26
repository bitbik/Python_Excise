#username.py
# simple string processing program to generate usernames.


def main():

	print "this program generates computer usernames. "
	print 

	#get user's first and last names 

	first = raw_input("please input the first name (all lowercase): ")
	last = raw_input ("please input the last name (all lowecases): ")

	#concatenate first initial with 7 chars of the last name.
	
	uname = first[ 0 ] + last[ : 7 ]

	#output the username
	print "your username is :", uname

main()



