def binarySearch(arr, start, end, target):
    if start > end:
        return -1

    mid = (start + end)//2

    if (arr[mid] == target):
        return mid

    if arr[mid] < target:
        return binarySearch(arr, mid+1, end, target)

    return binarySearch(arr, start, mid-1, target)


arr = [1, 2, 3, 4, 5, 6]
res = binarySearch(arr, 0, len(arr) - 1, 5)
print(res)
