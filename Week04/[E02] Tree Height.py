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
        def delete_data(start, data) :
            if start == None :
                print("Delete Error,",data,"is not found in Binary Search Tree.")
                return

            if data < start.get_data() :
                start.set_left(delete_data(start.get_left(), data))

            elif data > start.get_data() :
                start.set_right(delete_data(start.get_right(), data))

            else :
                if start.get_left() == None :
                    return start.get_right()

                elif start.get_right() == None :
                    return start.get_left()

                maxValue = start.get_left()

                while maxValue.get_right() != None :
                    maxValue = maxValue.get_right()

                start.set_data(maxValue.get_data())
                start.set_left(delete_data(start.get_left(), maxValue.get_data()))

            return start

        self.set_root(delete_data(self.get_root(), data))

    def find_min(self) :
        def recursion_min(root) :
            if root.get_left() == None :
                return root.get_data()
            return  recursion_min(root.get_left())

        return recursion_min(self.get_root())

    def find_max(self) :
        def recursion_max(root) :
            if root.get_right() == None :
                return root.get_data()
            return recursion_max(root.get_right())

        return recursion_max(self.get_root())

    def is_empty(self) :
        return True if self.get_root() == None else False

    def preorder(self) :
        def preorder_recursion(root) :
            if root == None :
                return

            print("->",root.get_data(),end=" ")
            preorder_recursion(root.get_left())
            preorder_recursion(root.get_right())

        preorder_recursion(self.get_root())

    def inorder(self) :
        def inorder_recursion(root) :
            if root == None :
                return
            
            inorder_recursion(root.get_left())
            print("->",root.get_data(),end=" ")
            inorder_recursion(root.get_right())

        inorder_recursion(self.get_root())

    def postorder(self) :
        def postorder_recursion(root) :
            if root == None :
                return

            postorder_recursion(root.get_left())
            postorder_recursion(root.get_right())
            print("->",root.get_data(),end=" ")

        postorder_recursion(self.get_root())

    def traverse(self) :
        if self.is_empty() :
            print("This is an empty binary search tree.")
            return

        print("Preorder:",end=" ")
        self.preorder()
        print()

        print("Inorder:",end=" ")
        self.inorder()
        print()

        print("Postorder:",end=" ")
        self.postorder()
        print()
    
    def isExist(self, data) :
        def find_data_recursion(root, data) :
            if root == None :
                return False
            if data < root.get_data() :
                return find_data_recursion(root.get_left(), data)
            elif data > root.get_data() :
                return find_data_recursion(root.get_right(), data)
            return True

        return find_data_recursion(self.get_root(), data)
    
    def height(self):
        def height_recursion(root):
            if root is None:
                return 0
            return 1 + max(height_recursion(root.get_left()), height_recursion(root.get_right()))

        return height_recursion(self.get_root())

def main():
    my_bst = BST()
    while True:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    
    print(my_bst.height())
main()

