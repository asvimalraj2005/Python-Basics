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
#
#
# Title() -> Returns string in title case 
str5="The world is beautiful"
print(str5.title())
#
#
# max(str) -> Returns the highest alphabetical character lexicographically
str6="ABCDEFYZ"
print(max(str6))
#
#
# min(str) -> Returns the lowest alphabetical character lexicographically 
str7="ABCDEFYZ"
print(min(str7))
#
#
# strip() -> Removes all leading and trailing whitespace in string 
str8="Hello Person 1"
print(str8.strip())
#
#
# rstrip() -> Removes all trailing whitespaces in string (After the string whitespace will get removed)
str9="Hello Person 2           "
print(str9.rstrip())
#
#
# lstrip() -> Removes all leading whitespaces in string (Before the string whitespaces will get removed)
str10="       Hello Person 3"
print(str10.lstrip())
#
#
# Lower() -> Converts all the characters in the string to the lowercase
str11="hello Hello"
print(str11.lower())
#
#
# Upper() -> Converts all the characters in the string to the uppercase
str12="hello"
print(str12.upper())
#
#
# len() -> Returns the length of the string 
str13="Hello world"
print(len(str13))
#
#
# isalnum() -> True if string has only one character and everything number if doesn't it's false 
str14="Person 01"
print(str14.isalnum())
#
#
# isalpha() -> True if string has only one number and everything character if doesn't it's false 
#
#
# isdigit() -> Returns True if string contains only digits and False otherwise
str15="007"
print(str15.isdigit())
#
#
# Ect 



