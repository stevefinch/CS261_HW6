class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None        

    def insert(self, child):
        if self.value == None:
            self.value = child.value
        elif child.value < self.value:
            if self.left == None:
                child.parent = self
                self.left = child
            else:
                self.left.insert(child)    
        else:
            if self.right == None:
                child.parent = self
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

    def in_order(self):
        answer = []    
        if self.left != None:
            answer.extend(self.left.in_order())    

        answer.append(self.value)

        if self.right != None:
            answer.extend(self.right.in_order())    

        return answer

    def pre_order(self):
        answer = []    

        answer.append(self.value)

        if self.left != None:
            answer.extend(self.left.pre_order())    

        if self.right != None:
            answer.extend(self.right.pre_order())    

        return answer

    def post_order(self):
        answer = []    

        if self.left != None:
            answer.extend(self.left.post_order())    

        if self.right != None:
            answer.extend(self.right.post_order())    

        answer.append(self.value)

        return answer

    def delete(self):
        i_am_left_child = self.parent.left == self 
        i_am_leaf = self.left == None and self.right == None
        i_am_only_child = self.parent.left == None or self.parent.right == None
       
        if i_am_leaf:
            if i_am_left_child:
                self.parent.left = None
            else:
                self.parent.right = None

        elif i_am_only_child:        
            self.parent.left = self.left
            self.parent.right = self.right
