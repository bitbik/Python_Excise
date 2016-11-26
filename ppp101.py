###############################################
#
#	dateconvert2.py
#
#	convert a date in into "mm/dd/yyyy" from
#	month day, year
# 	
#
##############################################

import string

def main():

	#get the day month and year

	day, month, year = input ("please enter day, month and year numbers: ")
	#dateStr = raw_input("Enter a data mm/dd/yyyy:")
	
	date1 = str(month) + "/" + str(day) + "/" + str(year)

	months= ["January","February","March","April","May","June","July","August","September","Octpber","November","December"]
	
	monthStr = months[month -1 ]

	date2 = monthStr+" " + str(day) + "," + str(year)

	#output the result

	print "the converted date is:", date1 , "or", date2 + "."


main()



