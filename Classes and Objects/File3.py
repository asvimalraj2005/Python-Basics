# Program to demonstrate the use of __getitem__() and setitem() methods
#
#
# class Numbers :                                   # Creating a class named Numbers
#       def __init__(self,myList):                  # Initialising a constructor for this class for creating an objects with the values passed inside the parenthesis when passed while creating the objects 
#               self.myList=myList                  # This line is used to assign the passed data strucutre to the objects 
#       def __getitem__(self,index):                # By using the __getitem__ method we are passing the index to it and returning back the element we needed from the array, where the index should not exceed array length
#               return self.myList[index]           
#       def __setitem__(self,index,val):            # By using the __setitem__ method we are updating the list values or we are appending the list elements 
#               self.myList[index]=val  
# NumList=Number([1,2,3,4,5,6,7,8])                 # Here the list is created 
# print(NumList[5])                                 # Directly calling the object associated method __getitem__ to print the value from the list 
# NumList[3]=10                                     # Setting up the value in the list by using the __setitem__
# print(NumList.myList)                             # Printing all the elements in the NumList 