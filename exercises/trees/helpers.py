import collections


class Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinaryTree():
    def __init__(self):
        self.root_node = None

    def add_node(self, node, parent=None, position=""):
        global parent, position

        parent = parent
        position = position

        if self.root_node == None:
            self.root_node = node

        else:
            self._add_node(node)

    def _add_node(self, node):
        global parent, position

        if node.left_child == parent or node.right_child == parent:
            if position == "left":
                parent.left_child = node

            elif position == "right":
                parent.right_child = node

        else:
            left_node = node.left_child
            right_node = node.right_child

            if left_node != None:
                self._add_node(left_node)

            if right_node != None:
                self._add_node(right_node)

    def show_me_in_bfs(self):
        global exploring_queue, visited_nodes_arr
        exploring_queue = collections.deque([self.root_node])
        visited_nodes_arr = [self.root_node]

        print("Root node: " + self.root_node.data)

        self._show_me_in_bfs(self.root_node)

    def _show_me_in_bfs(self, node):
        global exploring_queue, visited_nodes_arr

        if len(exploring_queue) == 0:
            return True

        else:
            exploring_queue.pop()
