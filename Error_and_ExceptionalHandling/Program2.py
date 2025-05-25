# Program with multiple except blocks
#
# Syntax for multiple except blocks 
#
# 
# try :
#     block of code you need to execute
# except (Exception value):
#     Print Statement or return keyword can be used to exit from the function 
# except (Exception value):
#     Print Statement or return keyword can be used to exit from the function 
# except (Exception value): 
#     Print Statement or return keyword can be used to exit from the function
# as far many except with exception value can be on how much do the python programming language consist of 
# 
# 
# Below is an simple program where two exception block is created 
try: 
    num=int(input("Enter the number : "))
    print(num)
except (KeyboardInterrupt):
    print("Number should be entered")
except (ValueError):
    print("Don't enter any special characters or alphabets")
#
#
# Output for the program 
#
# Enter the number : A 
# Don't enter any special characters or alphabets 
#
#
# Multiple exceptions in a single block
#
# Syntax for multiple exceptions in a single block 
# 
# except (Exceptional Value 1 , Exceptional Value 2 , Exceptional Value 3 , Exceptional Value 4 , Exceptional Value 5 , Exceptional value n ) :     
#           Print Statement
# 
# We can include multiple exceptional value this could lead whenever testing an application by using the following syntax with try-block statement we could able to find the first error inside the program but not the second error so for better identification we can simply use separate-separate exceptional block statement 
#
# Below is the program for multiple exception block 
# 
try : 
    num = int (input("Enter the number"))
    print(num)
except (KeyboardInterrupt,ValueError,TypeError):
    print("Please correctly enter the number or it will leads to error while the execution of the program")
#
#
# Output for the program --> Enter the number A 
# ---> Please correctly enter the number or it will leads to error while the execution of the program
#
# Output for the program --> Enter the number 1 
# ---> 1 
#
# Note using except without mentioning any specific exception is not a good programming language practice because it catches all exceptions and deos not mak the programmer identify the root cause of the problem
#
# The else clause : the try except block can have an else clause inside it , the else clause statement will be executed after when there is no error is raised in the try block 
#
# Below is the program where the program is integrated with an else block 
#
try: 
    file_1=open('File1.txt')
    str=file_1.readline()
    print(str)
except IOError:
    print("Error occurred program is exited")
else:
    print("Program is executed successfully")
#
#
# Output 1 : '1234'                                 <-- If the consist of contents inside it 
#            Program is executed successfully    
# Output 2 : Error occurred program is exited 
