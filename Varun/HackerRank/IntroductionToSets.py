def average(array):
    count = 0
    set_array = set(array)
    for i in range(0, len(set_array)):
        count = count + list(set_array)[i]
    result = count / len(set_array)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)