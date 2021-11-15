
class Node:
    def __init__(self, data):
        self.tooBig = None 
        self.big = None 
        self.small = None 
        self.data = data 

    def insert(self, data):
        if self.data:
            if data - self.data >=10:
                if self.tooBig is None:
                    self.tooBig = Node(data)
                else:
                    self.tooBig.insert(data)
            elif (data - self.data >= 0) and (data - self.data < 10):
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            else:
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
        else: 
            self.data = data
            
    def setToNone(self):
        self.tooBig = None
        self.big = None
        self.small = None
        self.data = None
        return self

    def traverseToList(self, result = None):
        if self.small is not None:
            self.small.traverseToList(result)
        result.append(self.data)
        if self.big is not None:
            self.big.traverseToList(result)
        if self.tooBig is not None:
            self.tooBig.traverseToList(result)
        return result

    def delete(self, data):
        allNodes = []
        allNodes = self.traverseToList(allNodes)
        self.setToNone()
        for node in allNodes:
            if node == data:
                continue
            if self.data is not None:
                self.insert(node)
            else:
                self.data = node
                

    def traversal(self):
        if self.small is not None:
            self.small.traversal()
        print(self.data)
        if self.big is not None: 
            self.big.traversal()
        if self.tooBig is not None:
            self.tooBig.traversal()        

# test case
root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)

print("Tree contents after insertion using the traversal():")
root.traversal()

root.delete(45)

print("Tree contents after deleting 45 using the traversal():")

root.traversal()