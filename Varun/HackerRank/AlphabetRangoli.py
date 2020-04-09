#AlphabetRangoli.py
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def print_rangoli(size):
#figure out the number of lines you need to print
    numberoflines = (size * 2) - 1
    print(numberoflines)

#figure out the width of each line - number of letters in the line times 2 minus 1 and number of dashes in the line times 2 - 2
    width = ((size * 2) - 1) + (((size * 2) - 1) - 1)
    print(width)

#figure out the smaller aphabet set
    sizealphabet = alphabet[0:size]
    sizealphabet.reverse()
    #backend = alphabet[1:size]
    #reversesizealphabet = str(reversesizealphabet) + str(backend)
    print(sizealphabet)
    #print(reversesizealphabet)

#initialize middleline
    #middleline = [numberoflines, width]
    printarray = [['-' for i in range(width)] for j in range(numberoflines)]
    
#figure out how to print the middle line
    for i in range(numberoflines):
        print(sizealphabet[size])
        for j in range(size):
            print(''.join(sizealphabet[size-j:size]))
        
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
