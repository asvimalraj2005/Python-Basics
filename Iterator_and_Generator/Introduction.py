# Iterator is an object which allows a programmer to traverse through all the elements of a sequence 
# (like list or tuple or any data structure with data inside them ). An iterator is related with two methods --iter() and __next__(). 
# These iterators are implemented by using classes and a local variable for iterating 
# iter() --> function is used to create an iterator containing an iterable object 
# next() --> function is used to call the next element in the iterable object 
# 
#
# Generators : it is another way of creating iterators 
# Generators uses yield function which passes the function execution and returns the processed value 
# on the next iteration , the yield function returns the current processed values to the main function 
# It does not exit from the function when it is returning an value 
# Below is an python program where the yield method is used to print from 1-4
#
#
def GeneratorFunction(A):                       # The Gererator function takes A=4 as input 
    for i in range(1,A+1):                      # Loop is executed from 1 to A+1 
        yield i                                 # yield method returns the every processed values from this function 
    
A=4
Result=GeneratorFunction(A)                     # (1) The first value will be stored here which is returned from the generator function  -->  (2) The second value is returned from the function and stored here  -->  ( 3 ) The third value is returned from the function and stored here and so on 
print("The number between 1 and 4 are")         
print(next(Result))                             # The first value will gets printed ( 1 )
print(next(Result))                             # The second value will gets printed ( 2 )
print(next(Result))                             # The third value will gets printed ( 3 )
print(next(Result))

