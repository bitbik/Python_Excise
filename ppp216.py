################################################################################


# quadratic5.py

# a program that computes the rel roots of a quadratic equation

# Illustrates use of the math librabry 

# Note: this program  crashes if the equation has no real roots
################################################################################

import math #make the main librabry availbalble

def main():

	print "\nthis program finds the real solutions to a quadratic"
	print


	try:
		a,b,c = input ("Please input the coefficients (a,b,c):") 

		discrim = b * b - 4 * a * c
		#if discrim >0:
			
		discRoot = math.sqrt(discrim)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)

		print 
		print "The solutions are:",root1,root2
		print 

	#elif discrim == 0:
	#	root = -b /(2 * a)
	#	print
	#	print "There is double root at:",root
	#	print
	#else:
	#	print
	#	print "There is no real roots"
	#	print

	except ValueError,excObj:
		
		msg = str(excObj)
		if msg == "match domain error":

			print "\nNo Real Roots"

		elif msg == "unpack tuple of wrong size":

			print "\nyou did not give the right number of coefficients"

		else: 
			print "\nsomething is wrong, Sorry !"


	except NameError:
		print "\nYou did not enter Three numbers."

	except TypeError:
		print "\nYour inputs were not all numbers"

	except SyntaxError:
		print "\nYour input was not in the correcr form. missing comma?"
		
	except:
		print "\nSomething went wrong, Sorry !"

main()
	



