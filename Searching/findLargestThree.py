# Time O(N) | Space O(1)
def findThreeLargestNumbers(array):
    largestThree = [None, None, None]
    for num in array:
        updateLargest(largestThree, num)
    return largestThree

def updateLargest(largestThree, num):
    if largestThree[2] is None or num > largestThree[2]:
        shiftAndUpdate(largestThree, num, 2)
    elif largestThree[1] is None or num > largestThree[1]:
        shiftAndUpdate(largestThree, num, 1)
    elif largestThree[0] is None or num > largestThree[0]:
        shiftAndUpdate(largestThree, num, 0)

def shiftAndUpdate(largestThree, num, idx):
    for i in range(idx + 1):
        if i == idx:
            largestThree[i] = num
        else:
            largestThree[i] = largestThree[i + 1]