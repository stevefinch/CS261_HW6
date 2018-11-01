class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None        

    def insert(self, child):
        if child.value < self.value:
            if self.left == None:
                self.left = child
            else:
                self.left.insert(child)    
        else:
            if self.right == None:
                self.right = child
            else:
                self.right.insert(child)    
