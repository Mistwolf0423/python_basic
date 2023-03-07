n = int(input())
arr = map(int, input().split())

def remove_n(list, n):
    arr_2 = [num for num in list if num != n]
    return arr_2

arr = list(arr)
arr_2 = remove_n(arr, max(arr))
print(max(arr_2))