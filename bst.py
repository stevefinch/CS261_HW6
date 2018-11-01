class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None        

    def insert(self, child):
        if self.value == None:
            self.value = child.value
        elif child.value < self.value:
            if self.left == None:
                self.left = child
            else:
                self.left.insert(child)    
        else:
            if self.right == None:
                self.right = child
            else:
                self.right.insert(child)    

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            if self.left == None:
                return None
            else:    
                return self.left.find(value)      
        elif value > self.value:        
            if self.right == None:
                return None
            else:    
                return self.right.find(value)

