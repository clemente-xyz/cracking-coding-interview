

import collections
from helpers import find_unvisited_neighbors_inorder, find_unvisited_neighbors, find_min_neighbor, mark_as_visited

# BFS pseudo code:
'''
bfs(node):
    set exploring_queue with node init
    set visited_nodes_arr with node init
    set node as visited

    _bsf(node)

_bfs(node):
    if exploring_queue is empty, then:
        return visited_nodes_arr

    else, then:
        remove node from exploring_queue

        set unvisited_neighbors_arr as find_unvisited_neighbors_inorder(node)
        set unvisited_neighbors_arr as visited

        add unvisited_neighbors_arr to exploring_queue
        add unvisited_neighbors_arr to visited_nodes_arr

        set node as first_node_at_queue(exploring_queue)

        _bfs(node)
'''

# BFS code:


def bfs(node1):
    global exploring_queue, visited_nodes_arr

    # First: most right element, Last: most left element
    exploring_queue = collections.deque([node1])
    visited_nodes_arr = [node1]

    node1.set_me_visited()

    _bfs(node1)

    return visited_nodes_arr


def _bfs(node):
    global exploring_queue, visited_nodes_arr

    if len(exploring_queue) == 0:
        return visited_nodes_arr

    else:
        exploring_queue.popleft()

        unvisited_neighbors = find_unvisited_neighbors_inorder(node)
        visited_neighbors = mark_as_visited(unvisited_neighbors)

        for i in visited_neighbors:
            exploring_queue.append(i)

        for i in visited_neighbors:
            visited_nodes_arr.append(i)

        if len(exploring_queue) == 0:
            return visited_nodes_arr

        node = exploring_queue[0]

        _bfs(node)


# DFS pseudo code:
'''
dfs(node):
    set exploring_stack with node init
    set visited_nodes_arr with node init
    set node as visited

    _dfs(node)

_dfs(node):
    if exploring_stack is empty, then:
        return visited_nodes_arr

    else, then:
        set unvisited_neighbors_arr as find_unvisited_neighbors(node)

        if unvisited_neighbors_arr is empty, then:
            remove node from exploring_stack

            set node as last node of exploring_stack

        else, then:
            set node as min of unvisited_neighbors_arr
            set node as visited

            add node to exploring_stack
            add node to visited_nodes_arr

        _dfs(node)

'''

# DFS code:


def dfs(node1):
    global exploring_stack, visited_nodes_arr

    # First: most right element, Last: most right element
    exploring_stack = collections.deque([node1])
    visited_nodes_arr = [node1]

    node1.set_me_visited()

    _dfs(node1)

    return visited_nodes_arr


def _dfs(node):
    global exploring_stack, visited_nodes_arr

    if len(exploring_stack) == 0:
        return visited_nodes_arr

    else:
        node = exploring_stack[-1]
        unvisited_neighbors = find_unvisited_neighbors(node)

        if len(unvisited_neighbors) == 0:
            exploring_stack.pop()

        else:
            node = find_min_neighbor(unvisited_neighbors)

            node.set_me_visited()

            exploring_stack.append(node)
            visited_nodes_arr.append(node)

        _dfs(node)
