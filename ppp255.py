###############################################

# average7.py



#############################################

import string

def main():

	fileName = raw_input("\n\nWhat file are the numbers in? ")
	infile = open(fileName,'r')

	sum = 0.0
	count = 0

	line = infile.readline()

	while line != "":
	
		# update the sum and count 

		for xStr in string.split(line):
			sum = sum + eval(xStr)
			count = count +1
		line =infile.readline()


	print "\nThe average of the numbers is ",sum/count


main()


			
	


