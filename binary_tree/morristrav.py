class Graph:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def morrisTrav(root):
    current = root

    while current is not None:
        if current.left is None:
            print(current.data)
            current = current.right
        else:
            pre = current.left
            while True:
                if pre.right is None:
                    pre.right = current
                    current = current.left
                    break
                if pre.right is current:
                    pre.right = None
                    current = current.right
                    break
                pre = pre.right


root = Graph(1,right=Graph(3),left=Graph(2, left=Graph(4),right=Graph(5)))

for v in morrisTrav(root):
    print(v, end=' ')
  


