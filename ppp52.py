#change.py
#a program to calculate the value of some change in dollars



def main():

	print "change counter "
	print 
	print "please input the count of each coin type." 
	quarters = input ("quarters: ")
	dimes = input ("dimes: ")
	nickels = input ("nickels: ")
	pennies = input ("pennies ")

	total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

	print 

	print "the total is : ", total

main()

 
