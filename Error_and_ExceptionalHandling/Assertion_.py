# An assertion is a basic check that can be turned on or off when the program is being tested 
# By using assert statement an exception is tested if the result of the expression is False then an exception is raised
# Assertions can be implemented by using assert statements , assertions are placed at the start of a fucntion to check for valid input, and after afunction call to check for valid input 
# Syntax for assertion is --> assert expression[ , arguments]
#
# In general if the assert keyword associated statement does not provide any error then it will provide any error which is raised by the AssertionError
# If the assert associated statement does provide any error during the execution of the program then the 'AssertionError' function will be used to raise 
# an exception that could stop the execution of the code or if the raised AssertionError function error will be provided as the output to the user by using 
# the yoeld method where the current execution of the program is stopped and returning the error after that it will resumed to execute the program
#
# Note : Assert statement should be used for trapping user-defined constraints 
# Program to use the assert statement 
#
# Division of two numbers 
A=int(input("Enter the number A "))
B=int(input("Enter the number B "))                        # The value A could not be divided by zero but it can be divided by any number(Integers condition based -infinity to +infinity)
assert(B!=0), "Invalid B input"                            # If the B value is equal to zero then the "Invalid B input" will be printed while on the process of executing the code
print("Quotient",A/B)                                      # If the B value is properly provided on the input function then there will no error is asserted and quotient of both the input A and input B is calculated 


# Input A = 10 
# Inpur B = 20
# Output Quotient -> 2

# Input A = 10
# Input B = 0
# Output Invalid B input 
>>>>>>> 6a44a1b90148d1c75203610bd109aec7566c8579
