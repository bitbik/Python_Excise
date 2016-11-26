#########################################
#
#  month.py
# a program to print the avvreviation of a month,
# given its number 
#



def main():

	#months is used as a lookup table
	months= "JanFebMarAprMayJunJulAugSepOctNovDec"
	
	n = input ("enter a month number (1-12):")

	# compute starting position

	pos = (n-1) * 3

	#Grab the starting position of month n in months

	monthAbbrev = months[pos:pos+3]

	# print result

	print ("the month abbreviation is :"), monthAbbrev + "."

main()



