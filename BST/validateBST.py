def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftisValid = validateBSTHelper(tree.left, minValue, tree.value)
    rightisValid = validateBSTHelper(tree.left, tree.value, maxValue)
    return leftisValid and rightisValid

### Time O(N) n = no of nodes
### Space O(D) d = depth of the tree [ len of longest branch will be on the call stack]