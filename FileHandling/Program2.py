# In here we are going to see how to read a file and write a file 
# The read() and write() are used to read data from file and write data to files respectively.
# write() method is used to write a string to an already opened file
# Note : The write method is does not add a newline character ('/n') to the end of the string 
# Below is the python program for writing the file 
#
file=open("File1.txt","w")                         # We are opening the file by the access mode of 'w' 
file.write("  \ ^_^ \" ")                          # The contents which has to get written here is written by using the function write(), file is the object 
file.close()                                       # close() function is used to close the file object after getting become modified
print("Data is written to the file")               # This statement is printed after the data is written on to the file 
#
#
# Note : The write method returns None
# 
# The writelines() method is used to write to list of strings 
#
# 
# Program to write to a file using teh writelines method 
# 
# 
file=open("File1.txt","w")                         # open method is used to open the file with the mode of write 
lines=["",""]                                      # Thus the list is created with the name of lines consist of the string ","
file.writelines(lines)                             # By using the writelines we are passing the list into the function and writing the lines 
file.close()                                       # By using close function we are closing the file object 
print("Data is written to the file")               # Notifying the user that the contents which are inside the list named lines are written inside the file 

