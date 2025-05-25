
# program to delete a file namde file1.py or pythonfile1.txt
import os                                                             # OS is the main module to be imported on to the python file for deleting it's content are remove the entire file and file contents 
os.remove("file1.txt")  (or)  os.remove("pythonfile1.txt")            # You can use any lines around the 'or' for to remove a file's content or delete a file entirely
print("File deleted")                                                 # Printing the statement that the file is deleted "File deleted"



# From the above code we can state by using the OS module and it's function 'remove' we are entirely removing the file1.txt / pythonfile.txt
# After deleting the program will print "File deleted" on the user's screen
# To double check it we must go the file's location and check the file is there or not (Most probably the file got deleted) 
