'''
Adding two polynomials using Linked List
Given two polynomial numbers represented by a linked list. Write a function that add
these lists means add the coefficients who have same variable powers.
Example:
Input:
1st number = 5x^2 + 4x^1 + 2x^0
2nd number = 5x^1 + 5x^0
Output:
5x^2 + 9x^1 + 7x^0
Input:
1st number = 5x^3 + 4x^2 + 2x^0
2nd number = 5x^1 + 5x^0
Output:
5x^3 + 4x^2 + 5x^1 + 7x^0

'''


class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

    def set_next(self, next_node):
        self.next = next_node
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get_head(self):
        return self.head
    
    def add_node(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)

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
                print(temp.coefficient,"X^",temp.exponent, sep="", end=" ")
                if temp.next is not None:
                    print("+", end=" ")
                temp = temp.next



def add_two_polynomial(p1,p2):
    p3 = LinkedList()
    p1 = p1.head
    p2 = p2.head

    while p1 is not None and p2 is not None:
        if p1.exponent > p2.exponent:
            p3.add_node(p1.coefficient, p1.exponent)
            p1 = p1.next
        elif p1.exponent < p2.exponent:
            p3.add_node(p2.coefficient, p2.exponent)
            p2 = p2.next
        else:
           p3.add_node(p1.coefficient+p2.coefficient, p1.exponent)
           p1 = p1.next
           p2 = p2.next

    print("Addition is: ")
    p3.display()
    print()



'''
l1 = LinkedList()
l1.add_node(5,3)
l1.add_node(4,2)
l1.add_node(2,0)
l1.display()

print()

l2 = LinkedList()
l2.add_node(5,3)
l2.add_node(4,2)
l2.add_node(2,0)
l2.display()
'''

l1 = LinkedList()
p1 = input("Enter first polynomial: ").split(" + ")
for p in p1:
    p = p.split("x^")
    l1.add_node(int(p[0]), int(p[1]))

print()

l2 = LinkedList()
p2 = input("Enter second polynomial: ").split(" + ")
for p in p2:
    p = p.split("x^")
    l2.add_node(int(p[0]), int(p[1]))

print()
add_two_polynomial(l1,l2)
print()