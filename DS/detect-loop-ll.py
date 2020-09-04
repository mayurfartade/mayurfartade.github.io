

class Node:
    def __init__(self, c):
        self.c = c
        self.next = None

    def set_next(self, next_node):
        self.next = next_node
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get_head(self):
        return self.head
    
    def add_node(self, c):
        new_node = Node(c)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def display(self):
        if self.head == None:
            print("Empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.c, end=" ")
                
                temp = temp.next
    
    # Floyd’s Cycle detection algorithm
    def detect_loop(self):
        temp = self.head
        slow_p = fast_p = temp
        pre = slow_p
        while slow_p and fast_p and fast_p.next:
            pre = slow_p
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("loop detected")
                print("Value at loop",pre.c)

                count = 1
                slow_p = slow_p.next
                while slow_p != fast_p:
                    count += 1
                 
                    slow_p = slow_p.next
                print("Loop Length is",count)
                #self.remove_loop(pre)
                return 0
        else:
            print("no loop detected")

    def remove_loop(self, pre):
        pre.next = None
        print("loop removed")


l1 = LinkedList()
l1.add_node(1)
l1.add_node(2)
l1.add_node(3)
l1.add_node(4)
l1.add_node(5)
#l1.display()

l1.head.next.next.next.next.next = l1.head.next
#l1.display()
l1.detect_loop()
#l1.display()