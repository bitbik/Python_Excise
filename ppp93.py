###################################

#numbers2text.py


###################################

import string 

def main():

	print "this program  converts a sequence of ASCII numbers into a string of text"

	print " the string of tect that it represents"

	print 

	#get the message to encode

	inString = raw_input ("please enter the ASCII-encodede message:")
	
	#loop through each substring and build ASCII message
	message=""
	
	for numStr in string.split(inString):
		asciiNum = eval(numStr)
		message = message + chr(asciiNum)

	print " the decoded message is :", message
	
main()



		
	












