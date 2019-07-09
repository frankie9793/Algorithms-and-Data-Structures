# Complexities: Time O(N) Space O(N)
# def maxSubsetSumNoAdjacent(arr):
#     if not len(arr):
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
#     maxSums = arr[:]
#     maxSums[0] = arr[0]
#     maxSums[1] = max(maxSums[0], maxSums[1])
#     for i in range (2, len(arr)):
#         maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + arr[i])
#     return maxSums[-1]

# ans = maxSubsetSumNoAdjacent([75, 105, 120 ,75, 90, 135])
# print(ans)


def maxSubsetSumNoAdjacent(arr):
    if not len(arr):
        return 
    elif len(arr) == 1:
        return arr[0]
    second = arr[0]
    first = max(second, arr[1])
    for i in range (2, len(arr)):
        currentMax = max(first, second + arr[i])
        second = first
        first = currentMax
    return first

ans = maxSubsetSumNoAdjacent([75, 105, 120 ,75, 90, 135])
print(ans)