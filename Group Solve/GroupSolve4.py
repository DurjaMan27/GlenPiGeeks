#GroupSolve4.py
#madam

def reverse(string): 
    string = string[::-1] 
    return string 
    
palindrome=input("Enter a palindrome: ")

palindromereverse = reverse(palindrome)
print(palindrome)
print(palindromereverse)

if palindrome == palindromereverse:
    print(1)
else:
    print(0)
