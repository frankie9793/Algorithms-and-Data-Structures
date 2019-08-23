# Time O(lgN) | Space O(1)
def binarySearch(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# Time O(lgN) | Space O(lgN)
def binarySearch(array, target):
    return binarySearchHelper(array, 0, len(array) - 1, target)

def binarySearchHelper(array, start, end, target):
    if end < start:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearchHelper(array, start, mid - 1, target)
    else:
        return binarySearchHelper(array, mid + 1, end, target)
