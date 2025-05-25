# Finally block
# The try block has another optional block finally block which is used to define the clean-up actions that must be executed under all circumstances.
# The finally block is always executed before leaving the try block. 
#
# Syntax for the finally block
#
# try : 
#    write your operations here
#    ----------------------
#    Due to any exception, operations written here will be skipped
# finally : 
#    This would always be executed 
#
# 
# Note : You cannot have an else block with a finally block 
# 
# Below is the python program that use try, except, and finally block all together
#
# try : 
#   print("Raising Exception")
# except : 
#   print("Program has error")
# finally : 
#   print("This block is always gets executed")
#
# Output :  Raising Exception
#           Program has error
#           This block is alwats gets executed 
#
