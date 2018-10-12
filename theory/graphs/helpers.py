def find_node_by_data_in_edge(data, nodes):
    for i in nodes:
        if i.data == data:
            return i


def nodes_arr_quicksort(nodes_arr):
    if len(nodes_arr) == 0:
        return nodes_arr
    else:
        pivot = nodes_arr[-1].data
        j = 0

        for i in range(0, len(nodes_arr)):
            if nodes_arr[i].data < pivot:
                nodes_arr[j], nodes_arr[i] = nodes_arr[i], nodes_arr[j]
                j += 1

        nodes_arr[j], nodes_arr[-1] = nodes_arr[-1], nodes_arr[j]

        left_side_nodes_arr = nodes_arr_quicksort(nodes_arr[:j])
        right_side_nodes_arr = nodes_arr_quicksort(nodes_arr[j+1:])
        left_side_nodes_arr.append(nodes_arr[j])

        return left_side_nodes_arr + right_side_nodes_arr


def find_unvisited_neighbors_inorder(node):
    unvisited_neighbors = []

    for i in node.neighbors:
        if i.visited == False:
            unvisited_neighbors.append(i)

    return nodes_arr_quicksort(unvisited_neighbors)


def mark_as_visited(unvisited_neighbors):
    visited_neighbors = []

    for i in unvisited_neighbors:
        i.visited = True
        visited_neighbors.append(i)

    return visited_neighbors
