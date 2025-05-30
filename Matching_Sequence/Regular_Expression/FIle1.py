# Problem description
# Program ro extract an email address from a text
# Below code for the above problem
#
# import re                                                        # Importing the re module
# pattern=r"[\w.-]+@[w.\]+"                                        # Making a pattern that is used to retrieve the gmail which is mixed from an regualar statement 
# string="Please send your feeback at info@oxford.com"             # Sentence that has gmail id in them
# match=re.search(pattern,string)                                  # Passing the pattern and string to the search module
# if match:                                                        # Using the if else statement 
#       print("Email",match.group())                               # If match is in the string then true
# else:                                                            # If not no matches in the statement
#       print("No match")                                          # Printing the no match 
#
# O/P : info@oxford.com                                            # The gmail address 
