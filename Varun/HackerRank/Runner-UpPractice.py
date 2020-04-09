#Runner-UpPractice.py

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(' ')))
        #map function is a function that takes the result and returns a list of variables after applying the given function
        #It is trying to take all the integers in the previous line and splitting it into different parts of an array

#x = max(arr)
#for x in arr:
    #x = max(arr)
    #arr.remove(x)
#print(max(arr))

x = max(arr)
while x == max(arr):
    arr.remove(x)
print(max(arr))