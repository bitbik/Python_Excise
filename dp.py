#########################################
#					#
#					#
#	 printfile.py			#
#					#
#	prints a file to the screen	#
#					#
#########################################

def main():


	fname = raw_input("Enter the filename: ")
	infile = open (fname,'r')
	data = infile.read()

	print data

main()




