# Built-In and User-Defined Exceptions
# There are lot of various built in exception that can be used to identify the errors in an program 
# Exception                     -->    Base class for all exceptions 
# StopIteration                 -->    Generated when the next() method of an iterator does not point to any object
# SystemExit                    -->    Raised by sys.exit() function
# StandardError                 -->    Base class for all built-in exceptions (Excludes StopIteration and SystemExit)
# ArithmeticError               -->    Base class for errors that are generated due to mathematical calculations
# OverflowError                 -->    Raised when the maximum limit of a numeric type is exceeded during a calculation
# FloatingPointError            -->    Raised when a floating point calculation could not be performed
# ZeroDivisionError             -->    Raised when a number is divided by zero
# AssertionError                -->    Raised when the assert statement fails
# AttributeError                -->    Raised when attribute reference or assignment fails
# EOFError                      -->    Raised when end-of-file is reached or there is not input of input() function
# ImportError                   -->    Raised when an import statement fails
# KeyboardInterrrupt            -->    Raised when the user interrupts program execution 
# LookupError                   -->    Base class for all liikup errors 
# IndexError                    -->    Raised when an index is not found in a sequence 
# KeyError                      -->    Raised when a ket is not found in the dictionary 
# NameError                     -->    Raised when an identifier is not found in local or global namespace
# UnboundLocalError             -->    Raised when an attempt is made to access a local variable in a function or method when no value has been assigned to it.
# IOError                       -->    Raised when input or output operation fails 
# SyntaxError                   -->    Raised when there is a syntax error in the program
# IndentationError              -->    Raised when there is an indentation problem in the program
# SystemError                   -->    Raised when an internal system error occurs 
# ValueError                    -->    Raised when the argument passed to a function are of invalid data type or searching a list for a non-existen value
# RuntimeError                  -->    Raised when the generated error does not fall into ant of the above category 
# NortImplementedError          -->    Raised when an abstract method that needs to be implmented in an inherited class is not implemeneted
# TypeError                     -->    Raised when two or more data types are mixed without coercion 

#  Consider the above excepts as VALUE
# Below is the code where the VALUE should be placed
# try :
#    code
# except (VALUE) :
#    Statement or code 
# else :
#    Statement or code
# finally : 
#    Statement or code will get compulsarilly executed by the compilet 
