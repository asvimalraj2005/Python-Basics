# Classes and Object
# Classes and Object are the two main aspects of object oriented programming
# A class is the basic building block in python
# A class creates a new type and object is na instance of the colass
# Classes provides a blueprint or a template using which objects are created 
# Every is an object or an instance of some class 
# All integer variable that we define in our program are actually instance of class int 
# All string variables are objects of class string
# Syntax of defining the classes 
#
# Class class_name :
#       <statement -1 >
#       <statement -2 >
#       <statement -3 >
#       <statement -4 >
# A class creates a new local namespace where all its attributes(data and function) are defined 
# object_name=class_name()
# Once a class is defined, the next job is to create an object(or instance) of that class.
# The object can then access class variables and class methods using the dot operator (.). The syntax to create an object is given as 
#
# Program to access class variable using class object 
# class ABC :
#      var = 10
# obj = ABC ( )
# print( obj . var )
# 
# O/P: 10
#
# In the above program, we defined a class ABC which has a variable var having a value of 10.
# The object of the class is created and used to access the ckass vaurbale using the dot operator. Thus we can think of a class as factory for making objects 
# 
# Data abstraction : Data abstraction is refer to the process by which data and functions are defined in such a way that only essential details are provided to the outside world and the implementation details are hidden
# Classes provide methods to the outside world to provide the functionality of the obj
# Data encapsulation defines different access levels for data variables and member functions of the class. These access levels specifies the access rights/
# (1) Any data or function with access level public can be accessed by any function belonging to any class/ This is the lowest level of data protection
# (2) Any data or function with access level private can be accessed by only accessed only by the class in which it is declared. This
#     is the highest level of data protection. Private variables are prefixed with a double underscore (__). For example, __var is a private variable of the class.
#
#
# Class method and self argument
# Class methods (or functions defined in the class) are exactly same as ordinary functions that we have been defining so far
# with just one small differences. CLass methods must have the first argument named as self. This is the first argument that is added to the beginning of the parameter list.
# You do not pass a value for this parameter then you call the method. The self argument refers to the object itself. The object that has called is the method. That means even if the method does not takes arguments 
# It should be defined to accept the self. 
# The class methods uses self, they require an object or instance of the class to be used. They are often reffered to as instance method
# Program to access class members using the class object 
# 
# class ABC ():                                  
#       var = 10
#       def display(self):
#           print("In class method....")
# obj = ABC ()
# print(obj.var)
# obj.display()
#
# Key points to remembers 
# The statements inside the class definitiion must be properly indented
# A class that has no other statements should have a passs statement at least
# The __init__() method --> Class Constructor
# The __init__() method is automatically executed when an object is created 
# The __init__() method is prefixed as well as siffixed by double underscores
# Syntax --> def __init__(self,[args...])
#
# Program illustrating the use of __init__() method
# class ABC ():
#   def __init__( self , val ) :
#       print(" In class method... ")
#       self . val = val
#       print(" The value is:" , val )
# obj = ABC ( 10 )
#
# The __init__() method accepts one argument val. , any other class method the first argument has to be self.
# __init__() method we define a variable as self.val which has exactly the same name as that specified in the argument list 
# The two variables have the same name, they are entirely different variables 
# The self.val belongs to the newly created object. 
# __init__() method is automatically involved when the object is creatd
#
#
#class variables and object varaibles 
# Class variables and object variables -> Class variables are owned by the class and object variables are owned by each object
# If a class has n object, then there will be n separate copies of the object variable as each object will have its own object variable
# The object variable is not shared between objects
# A change made to the object variable by one object will not be reflected in other objects.
# If a class has one class variable, then there will be copy only for that variable. All the objects of that class will share the class variable
# Since there exists a single copy of the class variable, any change made to the class variable by an object will be reflected in all other objects
# Class variables and object are ordinary variables that are bound to be class's and object's namespace respectively
#
#
# Program to differentiate between class and object variable 
# class ABC():
#   class_var = 0 
#   def __init__(self,var):
#       ABC.class_var=ABC.class_var+1
#       self.var=var
#       print("The object is :",var)
#       print("The value of class variable is :",ABC.class_var)
#
# obj1=ABC(10)
# obj2=ABC(20)
# obj3=ABC(30)
#
#
# 
        