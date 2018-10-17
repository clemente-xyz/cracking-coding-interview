from graphs import graph_generator, show_graph
from helpers import nodes_arr_quicksort
from index import dfs

graph = graph_generator([1, 2, 3, 4], [(1, 3), (3, 4), (3, 2), (4, 2)])

# show_graph(graph)

for i in dfs(graph[0]):
    print(i.data)
