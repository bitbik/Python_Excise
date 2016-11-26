######################################

# average5.py

######################################


def main():

	sum = 0.0
	count = 0
	
	fileName = raw_input("\n What is the name of the file? ")
	infile = open(fileName,'r')

	
	for line in infile:
		sum = sum + eval(line)
		count = count +1
	
	print "\nThe  average of the numbers is ", sum/count


main()
