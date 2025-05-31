    # Dictionary is a data structure where the values are stored in the format of keys and values 
    # Each key is separated from its value by a colon (:) and next consecutive values are separated by comma , 
    # Entire items are enclosed by { }
    # Syntax for the dictionary is 
    # dictionary_set = { key1 : value 1 ,
    #                    key2 : value 2 ,
    #                    key3 : value 3 }
    #
    # Keys in the dictionary should be unique and values are can be in anytype 
    # Dictionary are not sequences rather they are mappings 
    # 
    # Simple example for creating a dictionary 
    # Dictionary_one={}
    # print(Dictionary )
    # 
    # Example 
    # Dictionary_Example = { 'Roll_No':'15',
    #                        'Name':'Raun',
    #                        'Course':'Tech'}
    # print(Dictionary_Example)
    #
    # Accessing value from the dictionary data structure
    # Dictionary_Example = { 'Roll_No':'15','Name':'Raun','Course':'Tech'} 
    # print(Dict['Roll_No'])                                                <-- we can access the value inside the dictionary by using the dict name and the key value 
    # print(Dict['Name'])                                                   <--   Dictionary_Example       ['Roll_No']
    # print(Dict['Course'])                                                 |   Name of the dictionary    Name of the key 
    #
    # Dictionary_Example ['Mark'] = 70
    # print(Dictionary_Example) 
    # 
    # Dictionary updation 
    # Dictionary_Example['Course']='BCA'
    # print(Dictionary_Example)
    # 
    # Dictionary is an associative array also known as hashes since any key of the dictionary can be associated or mapped to a value 
    # 
    # We can del one or more values by using the del keyword 
    # def Dictionary_Example('Course')
    # the above deletes the key-value pair in the dictionary 
    # Dictionary_Example.clear()                                         <-- Deletes all the entries in the dictionary 
    #
    # Dictionary_Example.pop('Name')
    # 
    # Program to check a single key in the dictionary is present or not 
    # Dictionary_Example = {'Roll_no':'16/100',
    #         'Name':'Raun',
    #         'Course':'Btech'}
    # if 'Course' in Dictionary_Example:
    #           print(Dictionary_Example[Course])
    # else: 
    #           print("None")
    #
    # Sorting the items in dictionary 
    # print(sorted(Dictionary_Example.keys()))
    #
    # Looping a dictionary named Dictionary_Example
    # 
    # Dictionary_Example = {'Roll_no':'16/100',
    #         'Name':'Raun',
    #         'Course':'Btech'}
    # 
    # for key in Dictionary_Example:
    #           print(key)                               <-- Keys will get printed 
    #
    # for val in Dictionary_Example.value():
    #           print(val)                               <-- Values will get printed 
    #
    # for key,val in Dictionary_Example.items():         <-- Both the keys and values of the dictionary will get printed 
    #           print(key , val)
    #
    #