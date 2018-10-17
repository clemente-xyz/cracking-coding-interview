from graphs import graph_generator, show_graph
from helpers import nodes_arr_quicksort
from index import bfs

graph = graph_generator(
    [1, 2, 3, 4, 5], [(1, 2), (2, 3), (2, 4), (3, 4), (4, 5)])

# show_graph(graph)

for i in bfs(graph[0]):
    print(i.data)
