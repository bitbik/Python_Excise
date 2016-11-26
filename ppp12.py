t#file: chaos.py
# a simple program illustrating  a chaotic behavior.

def main():
	print "this program illustrate a chaotic function"
	x = input ("enter a number between 0 and 1: ")
	n = input ("how many numbers should i input ?")
	for i in range(n):
		x = 3.9 * x * (1 - x)
		print x

main() 
