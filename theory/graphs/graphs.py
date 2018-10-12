from nodes import nodes_generator
from helpers import find_node_by_data_in_edge

# Graph initiation:


def graph_generator(nodes_data, edges):
    nodes = nodes_generator(nodes_data)

    for i in edges:
        node_x = find_node_by_data_in_edge(i[0], nodes)
        node_y = find_node_by_data_in_edge(i[1], nodes)

        node_x.add_neighbor(node_y)
        node_y.add_neighbor(node_x)

    graph = nodes

    return graph

# Graph printing code:


def show_graph(graph):
    print("Graph: \n")

    for i in graph:
        print("Node: " + str(i.data))

        for j in i.neighbors:
            print("Neighbor: " + str(j.data))
