######################################################
#
# cball3.py
#
#
######################################################

from math import pi,sin,cos

class Projectile:

	def __init__(self,angle,velocity,height):
		self.xpos = 0.0
		self.ypos = height
		theta = pi * angle / 180.0
		self.xvel = velocity * cos(theta)	
		self.yvel = velocity * sin(theta)
		
	def update(self,time):

		self.xpos = self.xpos + time * self.xvel
		yvel1 = self.yvel - 9.8 * time
		self.ypos = self.ypos + time *(self.yvel +yvel1)/2.0
		self.yvel = yvel1

	def getY(self):
		return self.ypos

	def getX(self):
		return self.xpos

	
def getInputs():
	a = input("Enter the launch angle (in degrees):")
	v = input("Enter the initial velocity (in meters/sec):")
	h = input("Enter the initial height (in meters):")
	t = input("Enter the time inteval between position calculations:")

	return a,v,h,t

def main():

	angle,vel,h0,time = getInputs()
	cball = Projectile(angle,vel,h0)
	while cball.getY() >=0:
		cball.update(time)
	print "\nDistance traveled : %0.1f meters."%(cball.getX())

main()




