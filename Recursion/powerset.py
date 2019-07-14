# O(2^n * n) Time | O(2^n * n) Space
# Time complexities and space complexities are both 2^n * n, 2^n is the number of subsets with a given set of n elements can have
# multiplied by n which is the average number of elements inside each subset

# Algorithm: Initialize a subset with an empty set first, loop through each element in the array 
#            for each of the subsets currently in the subset array append the new element to each of it and add it to the subsets array
# Iterative approach
def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets


def powersetRecursive(array, Idx = None):
    if Idx is None:
        Idx = len(array) - 1
    elif Idx < 0:
        return [[]]
    ele = array[Idx]
    subsets = powersetRecursive(array, Idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets

# Example
# array = [1,2,3,4]
# Idx = 4 -1 = 3
# ele = array[3] = 4
# subsets = powersetRecursive(array, 2)...

# array = [1,2,3,4]
# ele = array[2] = 3
# subsets = powersetRecursive(array, 1)...

# array = [1,2,3,4]
# ele = array[1] = 2
# subsets = powersetRecursive(array, 0)...

# array = [1,2,3,4]
# ele = array[0] = 1
# subsets = owersetRecursive(array, -1)...

# Idx < 0 ? ==> True ==> return [[]]

# subsets = [[]]
# ele = 1
# execute double for loops ==> subsets = [[], [1]]
# return subsets 

# subsets = [[], [1]]
# ele = 2
# execute double for loops ==> subsets = [[], [1], [2], [1,2]]

# Execute the rest of the functions on call stack