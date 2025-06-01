# Inheritance --> Passing down the parents class attributes and methods that the child class can use 
# super() --> Function used to give access to the methods of a parent class. Returns a temporary object of a parent class when used 
# 
# class Rectangle:                                                  <-- Creating a class named rectangle 
#       def __init__(self,length,width):                            <-- Creating a constructor 
#               self.length=length
#               self.width=width
#
# class Square(Rectangle):                                          <-- Creating a class named Square by inheriting the Rectangle class 
#       super().__init__(length,width)                              <-- By using super method we can able to use the rectangle functions and access rectangle class functions
#       def area(self):
#           return self.length*self.width                           <-- Calculation of length * width is done here
#
# class Cube(Rectangle):                                            <-- Cube class with inherited rectangle class attributes and data 
#       def __init__(self,length,width,height):                     <-- Constructor of the cube class
#           super().__init__(length,width)                          <-- By using super() method we are accessing the rectangle class constructor 
#           self.height=height          
#       def volumn(self):                                           <-- Method within a Cube class
#           return self.length*self.width*self.height               <-- Returning the self.length * self.width * self.height 
#
# square=Square(3,3)
# cube=Cube(3,3,3)
# print(square.area())
# print(cube.volumn())
