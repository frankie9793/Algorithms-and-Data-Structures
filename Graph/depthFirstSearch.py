class Node:

    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, finalArray):
        finalArray.append(self.name)
        for child in self.children:
            child.depthFirstSearch(finalArray)
        return finalArray


#Time Complexity: O(V + E) where v is the vertices and e is the edges 
#because we explore all the nodes(i.e vertices) and all of it's children which can be determined by the no of edges

#Space Complexity: O(V) in the worst case scenario the tree will look like A-> B-> C -> D, ie a linked list
#and therefore it's the total number of nodes(i.e vertices) that will be pushed onto the call stack during recursive call