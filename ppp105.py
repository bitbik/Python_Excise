#	change2.py
#	A program to calculate the value of some change in dollars
#
#	This version represents the total cash in cents


def main():



	print "Change Counter "
	print
	
	print " Please input the count of each coin type"

	quarters = input ("Quarters:")
	dimes = input ("Dimes: ")
	nickels = input ("Nikels: ") 
	pennies = input ("Pennies: ")

	total = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1

	print 

	print "The total value of your change is $%d.%02d" % (total/100,total%100)

	print 
	print  
main()


  
