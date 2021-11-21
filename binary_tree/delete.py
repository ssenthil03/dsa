'''
    Delete the given node in the binary tree and swap it with the 
    deepest right-most node in the binary tree
'''



class Graph:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


    def inorder(self, root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)

    def deleteDeepest(self, root, dnode):
        if root is None:
            return
        
        q = []
        q.append(root)
        while (len(q)):
            temp = q.pop(0)
            if temp == dnode:
                temp = None
                return
            if temp.right:
                if temp.right == dnode:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left == dnode:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def deletion(self, root, key):
        if root == None:
            return
        if root.right == None and root.left == None:
            if root.key == key:
               return None
            else:
                return root
        
        keynode = None
        q = []
        q.append(root)
        while (len(q)):
            temp = q.pop(0)
            if temp.key == key:
                keynode = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if keynode:
            x = temp.key
            self.deleteDeepest(root, temp)
            keynode.key = x

if __name__ == '__main__':
    root = Graph(1)
    root.left = Graph(2)
    root.right = Graph(3)
    root.left.left = Graph(4)
    root.left.right = Graph(5)
    root.right.left = Graph(6)
    root.right.right = Graph(7)

    root.inorder(root)
    root.deletion(root, 2)
    print("\n")
    root.inorder(root)



    

        

