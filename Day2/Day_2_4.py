# Basic list operations                  <> Return is used for function calculated value to the main function where print function is used to print the value which is quoted
# 
# len()                 -> returns length of the list or prints
#
# concatenation()       -> Joins two list and prints
#
# repetition()          -> Repeats elements in the list by using * operator 
#
# in()                  -> Checks if the value is present in the list 
#
# not in()                -> checks if the value is not present in teh list 
#
# max()                 -> returns the maximum value in the list 
#
# min()                 -> returns the minimum value in the list 
#
# sum()                 -> returns the total sum of the list 
#
# any()                 -> returns true if any element of teh list is true
#
# list()                -> converts an iterable(tuple,string,set,dictionary) to a list 
#
# sorted()              -> returns a new sorted list. The original list is not sorted 
#
 
list1=['1','2','4','3','6','1','4','2','6','2']        # <-- The list is not sorted  
#
#
list2=[1,2,3]                                          # <-- this list is sorted 
#
print(len(list1))
#
#
print(list1+list2)
#
#
if '1' in list1: 
    print("It is ")
else:
    print("It is not ") 
#
#
if '10' not in list1 :
    print("10 is not present") 
else : 
    print("It is present")
#
#
print(max(list1))               # Maximum value of the list will get printer
#
#
print(min(list1))               # Minimum value of the list will get returned
#
#
print(sum(list2))               # Returns the sum of the list1
#
#
print(all(list1))
#
#
print(any(list1))               
#
#
print(sorted(list1))            # Returns the sorted list 
