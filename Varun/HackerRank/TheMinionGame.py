#TheMinionGame

def minion_game(string):
#create a vowell lookup list
    vlist = ['A', 'E', 'I', 'O', 'U']
#create a consonant lookup list
    clist = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
#create a list of the input string
    string_list = list(string)
    #print(string_list)
#initialize a input string vowel list
    string_vlist = []
#initialize a input string consonant list
    string_clist = []
#initialize a input string consonant word dictionary
    stuart_clist = []
#initialize a input string vowel word dictionary
    kevin_vlist = []
#iterate thru the input string list character by character
    for i in range(len(string_list)):
        #print(string_list[i])
# if the character is a vowel and it is not added to input string vowel list then add it
        if (string_list[i] in vlist) and (string_list[i] not in string_vlist):
            string_vlist.append(string_list[i])
# if the character is a consonant and it is not added to input string consonant list then add it
        elif (string_list[i] in clist) and (string_list[i] not in string_clist):
            string_clist.append(string_list[i])
#Go through input string list and find all combinations of substrings that start with a consonant
    for i in range(len(string_list)):
        #Check if this character is a consonant
        if string_list[i] in string_clist:
        #starting at this position i till the end of the input string find all string combinations
            for j in range(i+1, len(string_list)+1):
                #print(string_list[i:j])
                stuart_clist.append(''.join(string_list[i:j]))
        elif string_list[i] in string_vlist:
            for j in range(i+1, len(string_list)+1):
                #print(string_list[i:j])
                kevin_vlist.append(''.join(string_list[i:j]))
    if len(kevin_vlist) > len(stuart_clist):
        print("Kevin " + str(len(kevin_vlist)))
    elif len(kevin_vlist) < len(stuart_clist):
        print("Stuart " + str(len(stuart_clist)))
    else:
        print("Draw")
#print input string vowel and consonant list
    #print(string_vlist)
    #print(string_clist)
    #print(kevin_vlist)
    #print(stuart_clist)

if __name__ == '__main__':
    s = input()
    minion_game(s)