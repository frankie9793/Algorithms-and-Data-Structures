def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if currentNum > otherNum and sums[j] + currentNum >= sums[i]:
                sums[i] = currentNum + sums[j]
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i 
    return [sums[maxSumIdx], buildSequences(array, sequences, maxSumIdx)]

def buildSequences(array, sequences, currentIdx):
    finalSequence = []
    while currentIdx is not None:
        finalSequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(finalSequence))


#Time Complexity: O(N^2)
#Space Complexity: O(N)