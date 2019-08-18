# O(N) Time | O(NM) Space
def levinshteinDistance(str1 , str2):
    edits = [[x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        edits[i][0] = edits[i-1][0] + 1
    for row in range(1, len(str1) + 1):
        for col in range(1, len(str2) + 1):
            if str1[row - 1] = str2[col - 1]:
                edits[row][col] = edits[row - 1][col - 1]
            else:
                edits[row][col] = 1 + min(edits[row - 1][col - 1], edits[row - 1][col], edits[row][col - 1])
    return edits[-1][-1]

# O(N) Time | O(min(N,M)) Space
def levinshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for row in range(1, len(big) + 1):
        if row % 2 == 1:
            currentEdits = oddEdits
            prevEdits = evenEdits
        else 
            currentEdits = evenEdits
            prevEdits = oddEdits
        currentEdits[0] = row
        for col in range(len(small) + 1):
            if small[col] == big[row]:
                currentEdits[col] = prevEdits[col - 1]
            else:
                currentEdits[col] = 1 + min(currentEdits[col - 1], prevEdits[col], prevEdits[col - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]