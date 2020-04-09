#FindingThePercentage.py

a_dict = {'one': 1} # Here 'one' is the key. 
a_dict['two'] = 2 # Adds key 'two' which points to 2
print (a_dict['one'])
a_dict['three'] = 3
# prints 1  
if 'three' in a_dict:
    # To check whether a certain string exist as a key in the dictionary  
    print (a_dict['three'])
    print("Three is in the dictionary")
else:  
    print ("Three not there")
# prints Three not there
del a_dict['one']
# Deletes index 'one' and the value associated with it  
print (a_dict)
# prints {'two': 2}