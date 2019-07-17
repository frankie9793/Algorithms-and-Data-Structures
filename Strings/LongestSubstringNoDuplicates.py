# O(N) Time | O(min(N,A)) Space where A is the unique set of alphabets present in string
# Algorithm: Create a Hash Map that stores the last seen index of each character
#            Iterate through the string and if the char appears in last seen update the startIdx
#            Update longest string through every iteration 
#            Update lastSeen char in hash map every iteration
#            Return a sliced string ** NOTE: slicing does not include last index **

def longestSubstringNoDuplicates(string):
    lastSeen = {}
    longest = [0,1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]