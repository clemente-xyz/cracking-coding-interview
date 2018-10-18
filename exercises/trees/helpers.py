import collections


class Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.visited = False


class BinaryTree():
    def __init__(self):
        self.root_node = None

    def add_node(self, target_node, parent=None, position=""):
        global target_node_var, parent_var, position_var

        target_node_var = target_node
        parent_var = parent
        position_var = position

        if self.root_node == None:
            self.root_node = target_node_var

        else:
            self._add_node(self.root_node)

    def _add_node(self, node):
        global target_node_var, parent_var, position_var

        if node == parent_var:
            if position_var == "left":
                parent_var.left_child = target_node_var

            elif position_var == "right":
                parent_var.right_child = target_node_var

        else:
            left_node = node.left_child
            right_node = node.right_child

            if left_node != None:
                self._add_node(left_node)

            if right_node != None:
                self._add_node(right_node)

    def show_me_in_bfs(self):
        global exploring_queue, visited_nodes_arr

        self.root_node.visited = True

        exploring_queue = collections.deque([self.root_node])
        visited_nodes_arr = [self.root_node]

        print("Root node: " + str(self.root_node.data))

        nodechain = self.bfs(self.root_node)

        for i in nodechain:
            print("\nNode: " + str(i.data))

            if i.left_child != None:
                print("left child: " + str(i.left_child.data))

            if i.right_child != None:
                print("right child: " + str(i.right_child.data))

    def bfs(self, node):
        global exploring_queue, visited_nodes_arr

        if len(exploring_queue) == 0:
            return visited_nodes_arr

        else:
            exploring_queue.popleft()

            childs = set_node_childs_inorder(node)

            if len(childs) != 0:
                for i in childs:
                    i.visited = True
                    exploring_queue.append(i)
                    visited_nodes_arr.append(i)

            if len(exploring_queue) == 0:
                return visited_nodes_arr

            node = exploring_queue[0]

            self.bfs(node)

            return visited_nodes_arr


def set_node_childs_inorder(node):
    childs = []

    if node.left_child != None and node.right_child != None:
        if node.left_child.data < node.right_child.data:
            childs.append(node.left_child)
            childs.append(node.right_child)

        else:
            childs.append(node.right_child)
            childs.append(node.left_child)

    elif node.left_child == None and node.right_child != None:
        childs.append(node.right_child)

    elif node.right_child == None and node.left_child != None:
        childs.append(node.left_child)

    return childs


def initialize_binary_tree(root_node_data, nodes_data, edges):
    nodes_arr = []
    nodes_dic = {}

    for i in nodes_data:
        node = Node(i)

        nodes_arr.append(node)

        nodes_dic[i] = node

        if i == root_node_data:
            root_node = node

    binary_tree = BinaryTree()

    binary_tree.add_node(root_node)

    for i in edges:
        node = nodes_dic[i[0]]
        parent = nodes_dic[i[1]]
        position = i[2]

        binary_tree.add_node(node, parent, position)

    return binary_tree
