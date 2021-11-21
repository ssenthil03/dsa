# Insert the given key in the first available position when traversing by
# level order method

class Graph:
    def __init__(self, data) -> None:
        self.key = data
        self.left = None
        self.right = None
    
def push(temp, key):
    if not temp:
        temp = Graph(key)
    q = []

    node = Graph(key)
    q.append(temp)

    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = node
            break
        else:
            q.append(temp.left)
        
        if (not temp.right):
            temp.right = node
            break
        else:
            q.append(temp.right)

def preOrder(root):
    if root:
        print(root.key)
        preOrder(root.left)
        preOrder(root.right)

g = Graph(1)
g.left = Graph(2)
g.right = Graph(3)
g.left.left = Graph(5)
g.right.left = Graph(6)
g.right.right = Graph(7)
push(g, 4)
preOrder(g)