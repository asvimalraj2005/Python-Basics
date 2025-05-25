# The syntax of filter() function is --> filter(function,sequence)
# The filter() function creates a list from those elements of teh list for which a cunction returns True.
# Below is an example program where we are using an function to generate sequence of numbers that are divisible by 2 or 4 exclusively in an range 
# with the help of list comprehension 
#
def check(A):                                    # Function check will get the value A as 2 on start and it will get next iterative number after second function call by the global filter function 
    if (A % 2 == 0 or A % 4 ==0):                # If A is divisible by 2 or 4 then this function will return True and the number will get added into the list 
        return 1 

evens=list(filter(check,range(2,22)))            # This line creates a list named evens and calls the check function recursively until it reaches upto range of 22      
print(evens)


# The output looks like this --->   [2 , 4 , 5 , 8 , 10 , 12 , 14 , 16 , 18 , 20 ]  