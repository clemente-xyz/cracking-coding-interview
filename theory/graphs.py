# Node data structure code:
class Node():
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.neighbors = []

    def set_me_visited(self):
        self.visited = True

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


# Graph initiation code:
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

graph = [node1, node2, node3, node4]

# Graph printing code:


def show_graph(graph):
    print("Graph: \n")

    for i in graph:
        print("Node: " + str(i.data))

        for j in i.neighbors:
            print("Neighbor: " + str(j.data))


show_graph(graph)

# BFS pseudo code:
'''
bfs(node):
    set exploring_queue with node init
    set visited_nodes_arr with node init
    set node as visited

    _bsf(node)

_bfs(node):
    if exploring_queue is empty, then:
        finish
    
    else, then:
        remove_node(exploring_queue)

        set unvisited_neighbors_arr as find_unvisited_neighbors_inorder(node)
        set unvisited_neighbors_arr as visited

        add unvisited_neighbors_arr to exploring_queue
        add unvisited_neighbors_arr to visited_nodes_arr

        set node as first_node_at_queue(exploring_queue)

        _bfs(node)



'''

# BFS code:
