from importlib.abc import SourceLoader


def take_arr(arr):
    print(arr)
    temp_list = []
    for y in range(len(arr)):
        temp = []
        for x in range(0, len(arr[y]), 2):
            if x == 0:
                temp.append(max(arr[y][x:2]))
            else:
                temp.append(max(arr[y][x:x*2]))
        temp_list.append(temp)
    return temp_list        

def take_arr2(arr):
    temp_list = []
    for y in range(0, len(arr), 2):
        temp = []
        for x in range(len(arr[y])):
            if y == 0:
                temp.append(min(arr[y][x], arr[y+1][x]))
            else:

                temp.append(min(arr[y][x], arr[y+1][x]))
        temp_list.append(temp)
    return temp_list 

def solution(arr, k):
    for i in range(k):
        row_len, col_len = len(arr[0]), len(arr)
        if row_len == 1 and col_len == 1:
            return arr
        elif row_len >= col_len:
            arr = take_arr(arr)
            print(arr)
        else:
            arr = take_arr2(arr)
            print(arr)
    return arr

solution([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]], 2)