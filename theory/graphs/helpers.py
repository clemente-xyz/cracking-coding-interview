def find_node_by_data_in_edge(data, nodes):
    for i in nodes:
        if i.data == data:
            return i


def find_unvisited_neighbors_inorder(node):
    unvisited_neighbors = []

    for i in node.neighbors:
        if i.visited == False:
            unvisited_neighbors.append(i)

    return unvisited_neighbors.sort()


def mark_as_visited(unvisited_neighbors):
    visited_neighbors = []
