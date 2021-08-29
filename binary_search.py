"""
    start = 0
    end = 9
    mid = 4
    check if arr[mid] == target
      is 5 == 3 , no
    check if target < arr[mid]
        end = mid  - 1 # end becomes 3
    check if target > arr[mid] is 3 > 2
        start = mid  + 1


"""


# target = 3
# print(len(arr))
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    isAsc = arr[start] < arr[end]
    while start <= end:
        mid = int(start + (end - start) / 2)
        if target == arr[mid]:
            return mid
        if isAsc:
            if target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
desc_arr = arr[::-1]
target = 6
print(binary_search(arr, target))
print(binary_search(desc_arr, target))
