class BSTNode :

    def __init__(self, data=0) :
        self.data = data
        self.left = None
        self.right = None
    
    def get_data(self) :
        return self.data
    
    def set_data(self, data) :
        self.data = data
    
    def get_left(self) :
        return self.left
    
    def set_left(self, left) :
        self.left = left
    
    def get_right(self) :
        return self.right
    
    def set_right(self, right) :
        self.right = right


class BST :
    
    def __init__(self) :
        self.root = None

    def get_root(self) :
        return self.root
    
    def set_root(self, root) :
        self.root = root

    def insert(self, data) :
        def recursion_insert(root, data) :
            if root == None :
                return BSTNode(data)

            if data < root.get_data() :
                root.set_left(recursion_insert(root.get_left(), data))

            else :
                root.set_right(recursion_insert(root.get_right(), data))

            return root
        self.set_root(recursion_insert(self.get_root(), data))

    def delete(self, data) :
        pass

    def findMin(self) :
        pass

    def findMax(self) :
        pass

    def is_empty(self) :
        pass

    def preorder(self) :
        def preorder_recursion(root) :
            if root == None :
                return

            print("->",root.get_data(),end=" ")
            preorder_recursion(root.get_left())
            preorder_recursion(root.get_right())

        preorder_recursion(self.get_root())

    def inorder(self) :
        pass

    def postorder(self) :
        pass

    def traverse(self) :
        pass