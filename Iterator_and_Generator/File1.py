list1=[1,2,3,4]               # List with values inside them
it=iter(list1)                # By using the iter function we are iterating over the list1 through by using 'it' object 
print(it.__next__())          # Object 'it' finds the first value and prints it out by using the __next__() method              <-- 1 is printed
print(it.__next__())          # Object 'it' finds the next value inside the list by using the __next__() and prints it          <-- 2 is printed
print(it.__next__())          # Same goes for here too                                                                          <-- 3 is printed 
print(it.__next__())          # Same goes for here too                                                                          <-- 4 is printed 
print(it.__next__())          # The compiler executes this line too but it will provide error here 


# i.e
# list1  =  [1,2,3,4] 
# it_object  =  iter(list1)
# it_object is linked to list1 by using the iter where elements in the list1 is mapped to this it_object 
# By using the dot operator we are linking the it_object with iterator function 
# where for every iterator function we are moving from one element to other element 