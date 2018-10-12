import collections

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
'''
def bfs(node1):
    global exploring_queue, visited_nodes_arr

    # First: most right element, Last: most left element
    exploring_queue = collections.deque([node1])
    visited_nodes_arr = [node1]

    node1.set_me_visited()

    _bfs(node1)


def _bfs(node):
    global exploring_queue, visited_nodes_arr

    if len(exploring_queue) == 0:
        return exploring_queue

    else:
        exploring_queue.popleft()

        unvisited_neighbors = find_unvisited_neighbors_inorder(node)
        visited_neighbors = mark_as_visited(unvisited_neighbors)

        add_nodes_to_queue(visited_neighbors)
        add_nodes_to_arr(visited_neighbors)

        node = first_node_at_queue(exploring_queue)

        _bfs(node)


print(bfs(node1))
'''
