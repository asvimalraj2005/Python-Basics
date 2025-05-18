# Variable length arguments 
# In Some situations, it is not known in advance how many arguments will be passed to a function. In such 
# cases, Python allows programmers to make function calls with arbitrary (or any) number of arguments. When
# we use arbitrary arguments or variable-length arguments, then the function definition uses an
# asterisk (*) before the parameter name. Syntax for a function using variable arguments can be given as 
# Syntax for it 
# def functionname([ arg1 , arg2 ] *var_args_tuple ):
#       function statements 
#       return [expression]
#
# Example for the above syntax 
def func(arg1, *arg2):
    print(arg1)
    for element in arg2:
        print(element)
#
#
#
func("Python 1.1","Python 1.2","Python 1.3","Python 1.4","Python 1.5")
