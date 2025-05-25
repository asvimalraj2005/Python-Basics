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