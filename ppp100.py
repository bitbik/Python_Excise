###############################################
#
#	dateconvert.py
#
#	convert a date in form "mm/dd/yyyy" to 
#	month day, year
# 	
#
##############################################

import string

def main():

	#get the date
	dateStr = raw_input("Enter a data mm/dd/yyyy:")
	
	#split into component

	monthStr, dayStr, yearStr = string.split(dateStr,"/")

	#convert the monthStr to month name

	months = ["January","Feb","March","April","May","June","July","Aug","September",
		"Oct","Nov","December"]
	monthStr = months[int(monthStr)-1]

	#output the result in month , day, year format

	print "the converted date is:", monthStr, dayStr + ",", yearStr


main()



