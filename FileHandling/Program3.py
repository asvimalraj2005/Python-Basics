# Append() Method
# Append is used to write the data after the contents of the file i.e if the file is consisted of data then we append the data to the file we are trying to write, if the file doesn't have any data then we are newly updating the file with data 
# For to open a file for appending the data we must use the mode of 'a' or 'ab'
# Below is python code for appending the data to an existing file 
#
# 
file = open (" File1 . txt  " , " a " )                                                                    # Opening the file named 'File1.txt' with the mode of 'a' which means we are going to append the data set to the file
file . write( "\n The contents you would like to write in that file will be placed here by you  " )        # By using write function we are append the data which is enclosed in an double quotes, if you don't like to use that method just create a list and pass that list into function writelines 
file . close( )                                                                                            # After appending of data we are closing the file 
print( "Data is appended to that file " )                                                                  # printing the statement "Data is appended to the file"
#
#
# Read() and Readline() method
# This two above methods is used to read the contents in the file and prints them out on the screen 
# The syntax of Read() and Readline() is fileobj.read([count])
# The count parameter specifies that how many lines of bytes to be read from the contents of the files, if the count is not specified with any values or not added to the count, then the Read() method will read all the lines of the file and prints them out 
#
#                                                                                                                                                                                                                                                                                                                                             this r denotes raw string for not to get error                                                              
# Program to print the first 10 characters of the file1.txt                           <-------------- Well if you getting errors while trying to access the file through the filename and it's format then you should have to right click on the file you want to read and then copy the path of the file and paste into the -->  file = open (r"Location of the file with format", "r")    while this "r" denotes mode of access 
#
#
file=open("File1.txt","r")      # (or)    file=open(r"Location path of the file","r")
print(file.read(10))            # Specifying how many lines to be read and printed  or just use -----> print(file.read())  <---- this will read the entire file 
file.close()                    # After reading and printing now we are closing the file 

