
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right  = None

    def Insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.Insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.Insert(data)

    def Inorder(self):
        if self:
            if self.left:
                self.left.Inorder()
            print(self.data, end=" ")
            if self.right:
                self.right.Inorder()

    def Preorder(self):
        if self:
            print(self.data, end=" ")
            if self.left:
                self.left.Preorder()
            if self.right:
                self.right.Preorder()

def Depth(node):
    if node is None:
        return 0
    else:
        Dleft = Depth(node.left)
        Dright = Depth(node.right)
        
        if Dleft > Dright:
            return Dleft+1
        else:
            return Dright+1   
            

root = Node(10)
root.Insert(5)
root.Insert(3)
root.Insert(6)
root.Insert(15)
root.Insert(12)
root.Insert(20)

#root.Preorder()
print()
#root.Inorder()
print()
print(Depth(root))