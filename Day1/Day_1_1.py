# Program to add two numbers that ar given using command line arguments 
import sys            # Sys is a module in python that provides access to system specific parameters and functions and used mainly used for I/O streams 
a = int(sys.argv[1])  # Taking as the first input from the command line after calling the file name 
b = int(sys.argv[2])  # Taking as the second input after the space of the first input 
sum = a + b           # Summing them here
print( sum )          # Printing the sum here 
