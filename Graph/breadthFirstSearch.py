class Node:

    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def breadthFirstSearch(self, finalArray):
        queue = [self]
        while len(queue) > 0:
            currentNode = queue.pop(0)
            finalArray.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
        return finalArray
                
# O(V + E) Time | O(V) Space