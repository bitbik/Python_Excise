###############################################

# page 172
#futval_graph3.py

###############################################

from graphics import *

def drawBar(window, year, height):

	#Draw a bar in window starting at year with given  height 

	bar = Rectangle(Point(year, 0),Point(year+1,height))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(window)


def main():

	#Introduction

	print "This program plots the growth of a 10-year investment ."
	
	#Get principle and intrest rate

	principal = input("Enter the initial principle: ")
	apr = input("Enter the annualized interest rate(0.1 for 10%): ")

	#Greate a graphics window with labels on left edge

	win = GraphWin("Investment growth Chart", 640 , 480)
	win.setBackground("white")
	win.setCoords(-1.75,-200,11.5,10400)
	Text(Point(-1,0),'0.0K').draw(win)
	Text(Point(-1,2500),'2.5K').draw(win)
	Text(Point(-1,5000),'5.5K').draw(win)
	Text(Point(-1,7500),'7.5K').draw(win)
	Text(Point(-1,10000),'10.0K').draw(win)
	
	drawBar(win,0,principal)
	for year in range(1,11):
		principal = principal*(1+apr)
		drawBar(win,year,principal)

	raw_input("Press <enter> to quit.")
	win.close()

main()
	

	


