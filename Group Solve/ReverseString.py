#ReverseString.py

s=input("Enter your string: ")
# split first
a=s.split()
# reverse list
a.reverse()
# now join them
result = " ".join(a)
# print it
print(result)

