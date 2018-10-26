'''A class Circle has  to define and we have to calcute circumference and area if radius of the circle has been given with the help of 
Object Oriented programming'''

class Circle:

	pi = 3.14

 # Attributes of Class Circle
    def __init__(self,radius=1):

		self.radius = radius
	 # method for calculating Circumference of Circle
	 # defined a function for calculating circumference
    def get_circumference(self):
	    return self.pi * self.radius * 2 
	# method for calculating Area of circle
	# defined  a function for calculating Area
	def get_area(self):
		return self.pi * self.radius ** 2

chotu = Circle()

print('Radius is: ',chotu.radius)
print('Area of the Circle is:',chotu.get_area())
print('Circumference of the Circle is:',chotu.get_circumference())

