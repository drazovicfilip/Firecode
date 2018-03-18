class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder(self):
        return None

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_data(self):
        return self.data

    def addLeft(self, value):

        if self.left_child == None:
            self.left_child = BinaryTree(value)
        
        # If the left slot is taken, we need to make a new edge
        else:
            toInsert = BinaryTree(value)
            self.left_child.left_child = toInsert

    def addRight(self, value):

        if self.right_child == None:
            self.right_child = BinaryTree(value)
    
        # If the right slot is taken, we need to make a new edge
        else:
            toInsert = BinaryTree(value)
            self.right_child.right_child = toInsert

