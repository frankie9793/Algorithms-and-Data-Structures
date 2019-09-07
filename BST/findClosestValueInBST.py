def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inff"))

def findClosestValueInBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - currentNode.value) < abs(target - closest):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

### Complexities 

### Average: Time O(lgn) Space O(1)
### Worst:   Time O(n) Space(1)