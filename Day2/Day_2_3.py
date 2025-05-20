# Function to reverse a string
def reverse(str):
    new_str=''
    i=len(str)-1
    while i>=0:
        new_str=new_str+str[i]
        i=i-1
    return new_str

# This is a basic methodology where for reversing a string 

# Function to reverse a array
def reverseArray(A):                # Reversing the array in-place without using two-pointer technique 
    i=0
    n=len(A)-1                      # Total length subtract with 1 for indexing basis
    while i<n:                      # Condition 
        temp=A[i]                   # Storing the first element in the temp variable 
        A[i]=A[n]                   # Now the first index is empty ; now filling it with last element 
        A[n]=temp                   # Now the last index is empty ; now filling it with temp element 
        i=i+1                       # incrementing i by 1 for proceeding to next variable
        n=n-1                       # decrementing n by 1 for proceeding to next variable in reverse
    return A                        # After reversing ; we are returning A 

# Function to reverse a array in a range 
def reverseArrayRange(A,R1,R2):                         # Replacing those i with R1, and with R2 with n
    if R1==R2:
        return A
    elif R1<R2:
        while R1<R2:                                    # Base condition 
            temp=A[R1]                                  # Same as the reverse array approach 
            A[R1]=A[R2]
            A[R2]=temp
            R1=R1+1
            R2=R2-1
    return A                                            # Reversing the Array in range and returning it 



    

    
    
