from collections  import deque

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def BST(self):
        if self.root is None:
            return

        q = deque()

        q.append(self.root)

        while len(q):
            temp = q.popleft()

            print(temp.data, end=", ")

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            

t = Tree(1)

t.root.left = Node(5)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(2)

t.BST()