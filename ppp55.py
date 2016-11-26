############################################################
#quadratic.py
# a program compute the real roots of a quafratic equation .
# Illustrate use of math library.
# Note: this program crshes if the equation has no real roots
#
#
############################################################

import math # make math library available

def main():

	print " this program finds the real solutions of a quareatic"
	print 

	a, b, c = input ("Please enter the coefficients (a,b,c) :")

	discroot= math.sqrt( b * b - 4 * a * c )

	root1 = (-b + discroot )/( 2 * a )
	root2 = (-b - discroot )/( 2 * a )

	print 
	print ("Solutions are : "), root1, root2


	print 

	print math.pi
	print math.e




main()



