#################################################################
#
#	userfile.py
#	Program to create a file of username in batch mode
#	
#
################################################################

import string

def main():


	print "This program creates a file of usernamess from a"

	print "file of names."

	#get the file names

	infileName = raw_input ("What files are the names in ? ")

	outfileName = raw_input ("what file should the usernames go in ? ")


	#open the files 

	infile = open(infileName,'r')
	outfile = open(outfileName,'w')

	#process each line of the input file

	for line in infile:

		#get the first and last name from file

		first, last = string.split(line)

		# create the username

		uname = string.lower(first[0]+last[:7])

		#write the unames into output file

		outfile.write(uname+'\n')
	
	#close both files 

	infile.close()
	outfile.close()

				 
main()




