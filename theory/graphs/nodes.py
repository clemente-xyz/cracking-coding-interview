# Node data structure:
class Node():
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.neighbors = []

    def set_me_visited(self):
        self.visited = True

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


# Nodes initiation:
def nodes_generator(datas_arr):
    nodes = []

    for i in datas_arr:
        nodes.append(Node(i))

    return nodes


'''
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)


node1.add_neighbor(node3)
node3.add_neighbor(node1)
node3.add_neighbor(node4)
node4.add_neighbor(node3)
node3.add_neighbor(node2)
node2.add_neighbor(node3)
node4.add_neighbor(node2)
node2.add_neighbor(node4)

nodes = [node1, node2, node3, node4]
'''
