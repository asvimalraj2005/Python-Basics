# Map function 
# The map() function applies a particular function to every element of a list. It's syntax is same as teh filter fnunction
# Syntax is --> map ( function , sequence )
# After implying this function on a list, it will return a new modified list where the new modified list will have the condition based values inside it 
# For this function to get used, we should have sequence or list with numbers inside them 
# Below is an program that adds 2 to every values in a list 
#
def Value_2_Sequence(A):
    A=A+2
    return A


# Original List Values 
Original_List=[1,2,3,4,5,6,7]                               #
print("The original list is printed",Original_List)         # We are printing the list values 

new_list=list(map(Value_2_Sequence,Original_List))          # Creating a new list named new_list where we are using list function and map function, the map function is used to map the values properly inside the new_list where it is returned from the Value_2_Sequence function, inside this statement we are passing the function name and the original list 
print("Modified list is",new_list)

# The resultant output will be looking like this 
# Original List --> [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]     # For every number in the original list 2 is added to every number 
# Modified List --> [ 3 , 4 , 5 , 6 , 7 , 8 , 9 ]     # The modified list 
