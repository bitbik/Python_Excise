###########################################



###########################################

def main():

	filename = raw_input ("Enter file names:")

	infile = open(filename,'r')

	for i in range (5):

		line = infile.readline()

		print line[:-1]

	print "$$$$$$$$$$$"

	for j in range (5):

		line2 = infile.readline()

		print line2[:-1]

	infile.close()
main()


