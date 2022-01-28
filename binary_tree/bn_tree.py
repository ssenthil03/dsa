class Tree:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)
 
def preOrder(root):
    if root:
        print(root.key)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print("Inorder: ")
inOrder(root)
print("\nPost: ")
postOrder(root)
print("\nPre: ")
preOrder(root)