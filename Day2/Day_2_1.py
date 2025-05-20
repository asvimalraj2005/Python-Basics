# Now here the Built-In String Methods and Functions 
# Strings are built-in python objects
# Functions are used to modify the strings 
# There are various no of string functions 
# Let's see enumerate(str) -> Returns an enumerate object that lists the index and value of all the characters in the string as pairs 
str="Hello world"
print(list(enumerate(str)))     # Output : [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]
#
#
# isidentifier() is used for check whether it is a valid string or not 
str1="Hello"
print(str1.isidentifier())      # O/P -> True
#
#
# join(list) is used to join a list of strings using the delimiter with which the function is invoked
str2=['abc','abc']
print(str)
#
#
# Split(delim) -> returns a list of substring separated by the specified delimiter. If no delimiter is specified then by default if split string on all whitespaces character
str3="abc,def"
print(str3.split(','))  # O/P : ['abc', 'def'] it split the strings and convert them into list 
#
# 
# swapcase() -> Switches the case of every character(uppercase character becomes lowercase and vice versa)
str4="The world is Beautiful"
print(str4.swapcase())

