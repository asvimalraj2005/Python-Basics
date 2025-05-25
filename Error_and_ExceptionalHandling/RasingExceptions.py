# You can raise an exception by using the raise keyword 
# Syntax for raise exception is --> raise[Exception[,args[,traceback]]]
# Exception is the name of exception to be raised (example,TypeError). args is optional and specifies a value for the exception argument.
# If args is not specified, then the exception argument is None
#
# Below is the program to deluberately raise an exception 
# 
try:                                                            # Try block has code to get exected, when executing it may causes error accordingly 
    num=10                                                      # Assigning the value 10 to the variable 'num'
    print(num)                                                  # Printing the value here 
    raise ValueError                                            # This line of code will always raises the ValueError exception unconditionally  
except:                                                         # The except block catches all the errors, it's not the best practice but it will be better to catch a specific error by adding specific exception name after the except keyword 
    print("Exception is occurred, exiting from the program")    # Print statement will be printed whenever any errors occur
5