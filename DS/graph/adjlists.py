

class AdjNode:
    def __init__(self, node):
        self.vertex = node
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.nodes = [None] * vertices

    def add_edge(self, src, dest):
        new_node = AdjNode(dest)

        new_node.next = self.nodes[src]
        self.nodes[src] = new_node

        new_node = AdjNode(src)
        new_node.next = self.nodes[dest]
        self.nodes[dest] = new_node


    def printGraph(self):
        for i in range(self.vertices):
            print(i, "-> ", end=" ")
            temp = self.nodes[i]

            while temp:
                print(temp.vertex, end=", ")
                temp = temp.next

            print()

g = Graph(4)

g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,3)


g.printGraph()