#futval.py
# a program computes the value of an investment in 10 years

def main():

	print "this program calculates the future value "
	print "of a ten year investment"

	principle = input ("enter the initial principle: ")
	apr = input ("input apr :")

	for i in range(10):

		principle = principle * ( 1 + apr )

	print "the value in 10 years is :", principle

main()
