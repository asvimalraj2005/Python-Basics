# Problem Statement 
# Program that creates an iterator to iterate over a list of elements 
# Below is the python program 
#
#   
class Iterator:                                             # Creating a class named Iterator 
    def __init__(self,List1):                               # Creating a class constructor and passing the List1 here as the argument in the constructor 
        self.List1=List1                                    # Assigning the List1 to List1 class object; now the list1 is not a data structure here it is consider here as a object 
        self.index=0                                        # Initialising the index variable with 0, this index will be incremented by 1 by the __next__ method to iterate and print the next element 
    def __iter__(self):                                     # Returning the object 
        return self
    def __next__(self):                                     # __next__(self)    --> self represents the object that it holds and this method 
        if self.index>=len(self.List1):                     # accessing the index value if is greater than or equal to the lenght of List1
            raise StopIteration                             # If the index exceeds the length of the List1 we raising an exception
        Value=self.List1[self.index]                        # List1 contains the first element, second element, etc
        self.index=self.index+1                             # Incrementing the index by 1 
        return Value                                        # Returning the value here 

List1=[1,2,3,4,5]
it=Iterator(List1)                                          # It object is now stored with 1,2,3,4,5
for L in it:                                                # By using the loop we are printing the elements inside the 'it' object 
    print(L,end=" ")                                        # Printing the element 