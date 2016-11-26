#######################################

# moth2.py
# A program to print the month abbreviation,

# Given its number


######################################

def main():

	# months is used as a lookup table
	months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug",
			"Sep","Oct","Nov","Dec"]

	n = input("Rnter a number(1-12):")

	print "the month abbreviation is ",months[n-1]+"."

main()





