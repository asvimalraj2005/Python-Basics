# Error and Exceptional handling 
# when we write some programs it might be prone to errors due to misconceptional code errors or by syntatic errors (indentation)
# For this kind of problems we should have to use try-catch-finally methods to provoke any errors which is going to be printed on to the user screen from the compiler 
# 
# Syntax error --> below is an example
#
i=0
if i==0 print(i)
# 
# The output will be like this 
#
# 
# Traceback (most recent call last):
# File "c:\Users\asvim\AppData\Local\Programs\Python\Python39-32\lib\runpy.py", line 197, in _run_module_as_main
#   return _run_code(code, main_globals, None,
# File "c:\Users\asvim\AppData\Local\Programs\Python\Python39-32\lib\runpy.py", line 87, in _run_code
#   exec(code, run_globals)
# File "c:\Users\asvim\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\bundled\libs\debugpy\__main__.py", line 71, in <module>
#   cli.main()
# File "c:\Users\asvim\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\bundled\libs\debugpy/..\debugpy\server\cli.py", line 501, in main
#   run()
# File "c:\Users\asvim\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\bundled\libs\debugpy/..\debugpy\server\cli.py", line 351, in run_file
#   runpy.run_path(target, run_name="__main__")
# File "c:\Users\asvim\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\bundled\libs\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 309, in run_path
#   code, fname = _get_code_from_file(run_name, path_name)
# File "c:\Users\asvim\.vscode\extensions\ms-python.debugpy-2025.8.0-win32-x64\bundled\libs\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 283, in _get_code_from_file
#   code = compile(f.read(), fname, "exec")
# File "Z:\Python Basics\Python-Basics\Error_and_ExceptionalHandling\Introduction.py", line 8
#   if i==0 print(i)
#           ^
#
# 
#
#
# The other type of error is logic error, where the user implements or create an algorithm or logic to solve a particular problem after the process of implementing it, it might not seems to be get the work done due to logic error and wrong implementation of the code 
# For example of logic error is --> Index out of range , dividing an element value by zero ect 
# 
#
# Exceptions :  Even if a statement is syntically correct, it may still cause an error when executed. Such errorsthat occut at run-time are known as exceptions 
# In simple this exceptions will be formed when an program is executed, meanwhile in the process of execution it disrupts the flow of process and encounters a situation which it cannot deal with 
# Exception is an python object which represents error 
# So that exceptions should be handled by the error handling methods like try-catch-finally so to not to terminate the program, the other parts of the program can be executed 
# 
a=5/0 
print(a)
# 
# For the above two lines of code the error will be produced like this 
#
# Traceback ( most recent call last )
#  File "pyshell#5", line 1, in <module>
#      5/0
# ZeroDivisionError : integer division or modulo by zero 
#
#
# To handle exceptions try-except blocks are used 
# 
# syntax for try-except are 
# 
# try : 
#     statements
# except ExceptionName : 
#     statements 
#
#
# Process of it : Step 1 First the try block is executed where it contains block of code 
# Process 2 : If no exceptions occurs, the except block is skipped
# Process 3 : If an exception occurs, during the execution of any statement in the try block 
# then rest of the statements are skipped in the try block and if the except type matches exception named after the except keyword, the except block is executed and then execution continues after the try statemeny 
# If an exception occurs which does not match the exception named in the except block then it is passed on to outer try block, then the program is terminated with the outer message 
# 
# Below is sample program how to handle the error where an number is divided by zero and this program with out the try-catch blocks it provokes the error as 'Division by zero' 
# 
# 
def Divide(num,deno):
    try:                            # The try method contains the code which should have to get executed 
        quo=num/deno
        print("Quotient",quo)
    except ZeroDivisionError:       # If the try block provided error related to the name which is defined after the except keyword then this except block statement will be executed where as if the error is like the number could not be due to larger exponential values or anything then this error will be printed on the screen
        print("Denominator cannot be divided by zero") 

Divide(10/0)
#
#
# The program output will be like "Denominator cannot be divided by zero" 
#
#
# We can include multiple except blocks with related exception or error that can provided by the program when executed 
