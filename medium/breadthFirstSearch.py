class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
      queue = [self]
      result = []
      while len(queue > 0):
        currentNode = queue.pop(0)
        result.append(currentNode.name)
        for child in currentNode.children:
          queue.append(child)
      return array
