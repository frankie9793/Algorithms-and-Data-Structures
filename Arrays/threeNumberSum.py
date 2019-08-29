# Time O(N^2) | Space O(N)
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i] , array[left] , array[right]])
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                right -= 1
    return triplets