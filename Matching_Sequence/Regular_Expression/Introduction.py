# Regular expressions are a powerful tool for various kinda of string manipulation.
# Regular expressions are a domain specific language (DSL) that is present as a library in most of the modern preogramming languages 
# A regular expression is a special sequence of characters that helps to match or find strings in another string.
# Regular expressions can be accessed using the 're' module which comes as a part of the standard library 
#
# The match() function --> Match() function matches a pattern to a string with optional flags. The syntax of match() function is 
# re.match(pattern,string,flags=0)
# Different values of flags 
# Flag              Description
#  re.I             Case sensistive matching
#  re.M             Matches at the end of the line
#  re.X             Ignores whitespace characters
#  re.U             Interprets letters according to Unicode chatacter set 
# 
#
#
# import re
# string = "She sells sea shells on the sea shore"
#
# pattern1="sells"
#
# if re.match(pattern,string):
#       print("Match Found")
# else:
#       print(pattern1,"is not present in the string")
#
# patter2="She"
# if re.match(pattern2,string):
#       print("Match Found")
# else: 
#       print(pattern2,"is not present in the string")
#
# O/P : sells is not present in the string
#       Match Found 
#
# The search function :
#               We saw that even when the pattern was present in the string, None was returned because the match was done only at the beginning
# of the string. So, we have another function, i.e search(), in the re module that searches for a pattern anywhere in the string 
# The syntax of the search() functin can be given as
# Syntax :  re . search ( pattern , string , flags = 0 )
# 
# Program to demonstrate the use of search() function
# 
# import re
# string = "She sells sea shells on the sea shore"
# pattern = "sells"
# if re.search(pattern,string):
#       print("Match Found")
# else: 
#       print(pattern,"is not present in the string")
#
# O/P : Match Found 
# 
# The sub() function
# The sub() function in the re module can be used to search a pattern in the string and replace it with another
# pattern. The syntax of sub() function can be given as 
# Syntax : re.sub(pattern,rel,string,max=0)
# 
#
# Program to demonstrate the use of sub() function 
# import re
# string = "She sells sea shelss on the sea shore"
# pattern = "sea"
# repl = "ocean"
# new_string = re.sub(pattern,repl,string,1)
# print(new_string)
# 
#
# The findall() and finditer() function
# The findall() function is used to seach a string and returns a list of matches of the pattern in the string.
# If no match is found, then the returned list is empty. The syntax of match() function can be given as 
# Syntax : matchList = re.findall( pattern , input_str , flags = 0 )
# 
# Program to demonstrate the use of findall() function
# import re
# pattern = r"[a-zA-Z]+\d+"
# matches = re.findall(pattern,"LXI 2013,VXI 2015,VDi 20104,Maruti Suzuki Cars in India")
# for match in matches:
#       print(match,end=" ")
# 
# O/P :
#  LXI 2013  VXI 2015  VDI 20104
# The re.findall() function returns a list of substrings that match a pattern
#
# pattern = r"[a-zA-Z]+\d+", finds all patterns that begins with one or more characters followed by a space and then followed by one or more digits
# 
#
# Program to demonstrate the use of finditer() function
# import re
# pattern = r"[a-zA-Z]+\d+"
# matches = re.finditer(pattern,"LXI 2013, VXI 2015, VDI 20104, Maruti Suzuki Cars available with us")
# for match in matches:
#       print("Match found at starting index :",match.start())
#       print("Match found at ending index :",match.end())
#       print("Match found at starting and ending index",match.span())
#
# O/P : 
# Match found at starting index : 0
# Match found at ending index : 8
# Match found at starting and ending index : ( 0 ,8 )
# Match found at starting index : 10
# Match found at ending index : 18
# Match found at starting and ending index : ( 10 , 18 )
# Match found at starting index : 20
# Match found at ending index : 29
# Match found at starting and ending index : ( 20 , 29)
# 
# 
# The  match object returned by search(), findall(), and match() functions of the module take options to modify 
# the behaviour of the pattern match. Some matching functions are
# ^ Matches at the beginning of the line,
# $ Matches at the end of the line,
# [...] Mathces any single character except the newline character,
# [^...] Mathces any single character not in brackets,
# re* Matches 0 or more occurrences of regular expression,
# re+ Matches 1 or more occurrence of regular expression,
# re? Matches 0 or 1 occurrence of regular expression,
# re{n} Matches exactly n number of occurrences of regular expression,
# re{n,} Matches n or more occurrences of regular expression,
# re{n,m} Matches at least n and at most m occurrences of regular expression. 
