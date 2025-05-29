# In previously the __init__ method is used to initialize the objects 
# Where now below is an program where ot modify a mutable type attribute
# 
# class Number:                                # Here's the class Number
#       evens=[]                               # Class attribute data type - evens 
#       odds=[]                                # Class arrribute data type - odds 
#       def __init__(self,num):                # Here's the constructor 
#           self.num=num                       # Accessing every number passed through the object 
#           if num%2==0:                       # if the object number is even
#                Number.evens.append(num)      # It will now get now appended to the evens list 
#           else:   
#               Number.odds.append(num)        # if the object passed valued through the constructor is odd then it will be added to the odds list 
#
# N1=Number(10)                                # N1 object is created here with the constructor value of 10 
# N2=Number(20)                                # N2 object is created here with the constructor value of 20 
# N3=Number(30)                                # N3 object is created here with the constructor value of 30 
# N4=Number(40)