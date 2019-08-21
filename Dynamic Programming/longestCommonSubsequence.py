#Time = Space Complexity = O(NM * min(N,M))
def longestCommonSubsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for row in range(len(1, str2) + 1):
        for col in range(len(1, str1) + 1):
            if str1[col - 1] == str2[row - 1]:
                lcs[row][col] = lcs[row - 1][col - 1] + [str1[col - 1]]
            else:
                lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1], key = len)
    return lcs[-1][-1]


#Time = Space Complexity = O(NM)

def longestCommonSubsequence(str1, str2):
    lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for row in range(1, len(str2) + 1):
        for col in range(1, len(str1) + 1):
            if str1[col - 1] == str2[row - 1]:
                lcs[row][col] = [str1[col - 1], lcs[row - 1][col - 1][1] + 1, row - 1, col - 1]
            else:
                if lcs[row - 1][col][1] > lcs[row][col - 1][1]:
                    lcs[row][col] = [None, lcs[row - 1][col][1], row - 1, col]
                else:
                    lcs[row][col] = [None, lcs[row][col - 1][1], row, col - 1]
    return buildSequence(lcs)

def buildSequence(lcs):
    sequence = []
    row = len(lcs) - 1
    col = len(lcs[0]) - 1
    while row != 0 and col != 0:
        currentEntry = lcs[row][col]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        row = currentEntry[2]
        col = currentEntry[3]
    return list(reversed(sequence))