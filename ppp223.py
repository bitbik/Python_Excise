######################################

# program maxn.py


# find the max number of a serious number
########################################

def main():

	n = input("\nHow many numbers are there ?")

	#set max to be the first value

	max = input("\nEnter a number >> ")

	# Now compare the n -1 sucessive numbers

	for i in range(n-1):

		x = input("\nPlease enter the number>> ")

		if max<=x:
			max=x

		

	print "\nThe max number is ", max 


main()
