# Lambda Functions or Anonymous Functions 
# Lambda or anonymous functions are so called because they are not declared as other functions using 
# the def keyword. Rather, they are created using teh lambda keyword. Lambda function are thrown-away
# function i.e they are just needed where they have been created and can be used anywhere a fucntion is required
# Syntax for lambda function --> lambda arguments : expression
# Below is the code for above statements 
Addition = lambda A,B: A+B
print(Addition(4,4))
print(Addition(5,5))
print(Addition(10,10))

# Lambda function assigned to variable twice
twice = lambda A : A * 2
print(twice(10))

# Lambda function not assigned ti bay variable twice
print((lambda A : A*2)(8))

