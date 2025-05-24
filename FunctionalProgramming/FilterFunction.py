# The syntax of filter() function is --> filter(function,sequence)
# The filter() function creates a list from those elements of teh list for which a cunction returns True.
# Below is an example program where we are using an function to generate sequence of numbers that are divisible by 2 or 4 exclusively in an range 
# with the help of list comprehension 
#
def check(A):
    if (A % 2 == 0 or A % 4 ==0):
        return 1 

evens=list(filter(check,range(2,22)))
print(evens)
