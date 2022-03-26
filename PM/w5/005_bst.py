class Node:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    @staticmethod
    def create_node(val, left = None, right = None):
        return Node(val, left, right)
    
    def insert_node(self, val):
        if self.data == val:
            return self
        elif val < self.data:
            if self.left:
                self.left = self.left.insert_node(val)
            else:
                self.left = self.create_node(val)
        else:
            if self.right:
                self.right = self.right.insert_node(val)
            else:
                self.right = self.create_node(val)
        return self
    
    def inorder_traversal(self):
        if(self.left):
            self.left.inorder_traversal()
        print(self.data)
        if(self.right):
            self.right.inorder_traversal()


mynode = None

q = 0
while q == 0 or q == 1:
    q = int(input("Enter 0 for insertion, 1 for inorder, any other for exit = "))
    if q == 0:
        val = int(input("Enter value to insert = "))
        if mynode:
            mynode.insert_node(val)
        else:
            mynode = Node(val)
    elif q == 1:
        mynode.inorder_traversal()