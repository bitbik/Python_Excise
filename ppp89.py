#############################
# text2numbers.py
# A program to convert a textual message into a sequence of numbers,
# utilizing the underlying ASCII encoding
#
#
####################################################################

def main():

	print "this program converts a textual message into a sequence"
	print "of numbers representing the ASCII encoding of the message."
	print

	#Get the message to encode

	message = raw_input("please enter the message to encode: ")

	print
	print "here are the ASCII code"

	#Loop through the message and print out the ASCII values for ch in message

	for ch in message:
		print ord(ch), #use comma to print all on one line

	print


main()

