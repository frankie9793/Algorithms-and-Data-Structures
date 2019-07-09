def invertBinaryTree(tree):
    queue =[tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftandRight(current)
        queue.append(current.left)
        queue.append(current.right)


def swapLeftandRight(tree):
    tree.right, tree.left = tree.left, tree.right


def invertBinaryTree(tree):
    if tree is None:
        return 
    swapLeftandRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)