class BSTNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

class BST :
    def __init__(self) :
        self.root = None

    def loop_insert(self) :

        n = input()
        if n == "End" :
            return 

        def recursion_insert(root, data) :
            if root == None :
                return BSTNode(data)

            if data < root.data :
                root.left = recursion_insert(root.left, data)

            else :
                root.right = recursion_insert(root.right, data)

            return root

        self.root = recursion_insert(self.root, int(n))
        self.loop_insert()
    
    def find_min(self) :
        def recursion_min(root) :
            if root.left == None :
                return root.data
            return  recursion_min(root.left)

        return recursion_min(self.root)

    def find_max(self) :
        def recursion_max(root) :
            if root.right == None :
                return root.data
            return recursion_max(root.right)

        return recursion_max(self.root)

def main() :
    myBST = BST()
    myBST.loop_insert()
    print("Max:",myBST.find_max())
    print("Min:",myBST.find_min())
main()