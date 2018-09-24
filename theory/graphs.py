# Depth First Search pseudo-algorithm:
'''
pending: solve what to do when all neighbors have equal value

main_dfs(graph):
    set randomly starting node as first_node
    call dfs(first_node, graph)

dfs(node, graph):
    if node is not visited, then:
        mark node as partially visited
        set start time

        if there are not visited neighbors, then:
            set lower not visited neighbor as next_node
        
        else, then:
            set lower partially visited neighbor as next_node
        
        call dfs(next_node)
    
    else if node is partially visited, then:
        set previous node as fully visited
        set finish time for previous node
        
        if there are not visited neighbors, then:
            set lower not visited neighbor as next_node
        
        else, then:
            if there are partially visited neighbors, then:
                set lower partially visited neighbor as next_node
            
            else, then:
                if (finish time of previous node + 1)*0.5 = total number of nodes in the graph, then:
                    set node as fully visited
                    finish algorithm
                else, then:
                    return error

        call dfs(next_node)

        

'''

# Depth First Search algorithm:


class Node():
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.availability = 0
        self.start_time = 0
        self.finish_time = 0

    def list_my_neighbors_availability(self):
        the_neighbors = []

        for i in self.neighbors:
            the_neighbors.append(i.availability)

        return the_neighbors

    def define_my_not_visited_lower_neightbor(self):
        not_visited_neighbors_data = []

        for i in self.neighbors:
            if i.availability == 0:
                not_visited_neighbors_data.append(i.data)

        lower_neightbor_data = min(not_visited_neighbors_data)

        for j in self.neighbors:
            if j.data == lower_neightbor_data:
                lower_neightbor_obj = j

        return lower_neightbor_obj

    def define_my_visited_lower_neightbor(self):
        visited_neighbors_data = []

        for i in self.neighbors:
            if i.availability == 1:
                visited_neighbors_data.append(i.data)

        lower_neightbor_data = min(visited_neighbors_data)

        for j in self.neighbors:
            if j.data == lower_neightbor_data:
                lower_neightbor_obj = j

        return lower_neightbor_obj


class Graph():
    def __init__(self):
        self.nodes = []

    def add_node(self, node_data, neighbor_of=None):
        new_node = Node(node_data)
        self.nodes.append(new_node)

        if neighbor_of:
            for i in neighbor_of:

                for n in self.nodes:
                    if n.data == i:
                        new_node.neighbors.append(n)
                        n.neighbors.append(new_node)

    def show_me(self):
        for n in self.nodes:
            print("Node: " + str(n.data) + " Status: " +
                  str(n.availability) + ", Neighbors: ")

            if len(n.neighbors) == 0:
                print("None")

            else:
                for m in n.neighbors:
                    print(str(m.data))

    def _dfs(self, node):
        global time

        if node.availability == 0:
            node.availability = 1
            # ignore this linting issue (Undefined variable 'time'), in not a bug
            time += 1
            node.start_time = time
            neighbors = node.list_my_neighbors_availability()

            if 0 in neighbors:
                lower_neighbor = node.define_my_not_visited_lower_neightbor()
                self._dfs(lower_neighbor)

            else:
                lower_neighbor = node.define_my_visited_lower_neightbor()
                self._dfs(lower_neighbor)

        elif node.availability == 1:
            time += 1

            for n in self.nodes:
                if n.start_time == time-1:
                    previous_node = n

            node.start_time = time
            previous_node.availability = 2
            neighbors = node.list_my_neighbors_availability()

            if 0 in neighbors:
                lower_neighbor = node.define_my_not_visited_lower_neightbor()
                self._dfs(lower_neighbor)

            else:
                if 1 in neighbors:
                    lower_neighbor = node.define_my_visited_lower_neightbor()
                    self._dfs(lower_neighbor)

                    return True

                else:
                    return False

    def dfs(self):
        first_node = self.nodes[0]
        global time
        time = 0
        self._dfs(first_node)


# Depth First Search algorithm testing:
'''
graph = Graph()

graph.add_node(1)
graph.add_node(2, [1])
graph.add_node(3, [1])
graph.add_node(5, [1])
graph.add_node(4, [3])
graph.add_node(6, [5])
graph.add_node(7, [6, 2])

graph.dfs()
graph.show_me()
'''
