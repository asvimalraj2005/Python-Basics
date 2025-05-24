# Python has many function and inbuilt modules that are used for manipulating and modifying the contends inside it 
# The first step for reading or writing it must be opened and after that you can perform any operations you needed to and lastly you must close the file 
# 
# Open() function 
# The open() function helps us to open the file by creating the file object, which will invoke methods associated with it -> The file object can be read, write, append etc (Generally these are the operations can be done, if you need you can overwrite the file or delete the contents of the file, copy the contents of the original file to the duplicate file)
# The syntax for the open() function is ---> fileobj=open(file_name[,access_mode])
# file_name is the name of the file you want to access 
# access_mode is the operation done on the file which leads you to modify it or does the access mode's operation you are preffered to use 
# There are lot of access_mode namely
#
#       r        -->    It is used to read a file
#       rb       -->    This is used to read the file in an binary format where it uses a file pointer which is placed in the beginning of the file 
#       r+       -->    This mode opens the file for both reading and writing where the file is opened by placing the pointer infront of the file 
#       w        -->    This mode opens the file where if the file is already existed then the contents of the file is overwritten, if the file name is does not exist then an new file is created under the name of this and new contents is added to it 
#       wb       -->    This mode opens the file in binary format for writing only if the file exists contents are over-written if not the new file under this name is created and new contents are appended according to the user needs  
#       w+       -->    Opens the file for both reading and writing : exists  -->  Overwritten  ( if not )   newfile is created --> contents are appended to it 
#       a        -->    Opens the file for appending the data to it, the pointer is placed at the end of the file : where exists  -->  data is appended  ( if not )   newfile is created --> contents are appended to it 
#       ab       -->    Opens the file in binary format [pointer is placed at the end of the file if exists ] :  exists  -->  new data is appended to the end   ( if not )   newfile is created --> contents are appended to it 
#       a+       -->    Opens the file for both reading and writing  :  exists  -->  new data is appended  ( if not )   newfile is created --> contents are appended to it 
#       ab+      -->    Opens the file in binary format for both reading and writing  : exists  -->  Pointer is placed at end of the file  ( if not )   newfile is created --> contents are appended to it  
#
# File Object Attributes 
#
# fileobj.closed()  --> Returns True if the file object is properly closed
# fileobj.mode()    --> Returns the access mode that is used to access the file
# fileobj.name()    --> Returns name of the file
