#MergeTheTools.py

def merge_the_tools(string, k):
#Find length of string
    n = len(string)
#Convert string into list
    list_string = list(string)
    substrings = []
    result_substrings = []
#Iterate through list to create substrings, in chunks of k
    for i in range(0, n, k):
        substrings.append(string[i:k+i])
    #print(substrings)
    for i in range(k):
        result_substrings_instance = []
        for j in range(len(substrings[i])):
            #print(substrings[i][j])
            #If the List is Empty, add the first letter
            if not result_substrings_instance:
                result_substrings_instance.append(substrings[i][j])
            #If the list isn't empty,
            elif result_substrings_instance:
                #If the letter isn't there, append to the list
                if substrings[i][j] not in result_substrings_instance:
                    result_substrings_instance.append(substrings[i][j])
                #If the letter already exists, move to next letter
                #do Nothing
        #result_substrings.append(''.join(result_substrings_instance))
        print(''.join(result_substrings_instance))
    print(result_substrings)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)