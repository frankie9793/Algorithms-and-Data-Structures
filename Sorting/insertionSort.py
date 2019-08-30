# Time O(N^2) | Space O(1)
def insertionSort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array