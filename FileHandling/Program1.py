# Program to open a file and print it's attribute values           <--- Main disclosure mentioned here is attributes
#
file=open("File1.txt","wb")                                         # In here we can define the file's path we want to access or the file name which we want to access 
print("Name of the file",file.name)                                 # This line is used to print the name of the file we are opening 
print("File is closed",file.closed)                                 # This line is used to print whether the opened file is closed properly or not; if not it returns the boolean value False otherwise it returns True 
print("which mode is used to open the file",file.mode)              # This line is used to print which mode is used to access the file 
#
# Program to access a file after it is closed                      <--- Conveys that if we try to access the file object after it got closed it provided error
#
file=open("File1.txt","wb")                                         # This method opens the file in the mode of writing in binary format : if the file exists the contents are overwritten , if not new file with same name passed on the open method is created 
print("Name of the file",file.name)                                 # This line is used to print the name of the file
print("File is closed ",file.closed)                                # This line is used to check whether the file is closed or not 
print("File is closed by using the close method")                   # This line prints the notation of file is being closed by using the close() method 
file.close()                                                        # close() method is used here to close the files 
print(file.read())                                                  # After the file is being closed by using the close() method, the user tries to access the contents inside the file -> this line leads or provoke errors 

