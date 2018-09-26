# Binary tree creation and manipulation algorithm:


class Node():
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.level_at = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert_node(self, data):  # Filled by width prioritizing by left nodes

        if self.root:
            current_node = self.root
            current_level = 1

            while True:
                if current_node.left_node:
                    if current_node.right_node:
                        current_node = current_node.left_node
                        current_level += 1
                    else:
                        current_node.right_node = Node(data)
                        current_node.right_node.level_at = current_level
                        break

                else:
                    current_node.left_node = Node(data)
                    current_node.left_node.level_at = current_level
                    break

        else:
            self.root = Node(data)
            self.root.level_at = 0

    def show_me(self):
        if self.root:
            current_node = self.root
            print("Root: " + str(current_node.data) +
                  " at level: " + str(current_node.level_at))

            while True:
                if current_node.left_node:
                    print("Left node: " + str(current_node.left_node.data) +
                          " at level: " + str(current_node.left_node.level_at))

                    if current_node.right_node:
                        print("Right node: " + str(current_node.right_node.data) +
                              " at level: " + str(current_node.right_node.level_at))
                        current_node = current_node.left_node

                else:
                    break

        else:
            print("Empty tree")


tree = BinaryTree()
tree.insert_node(9)
tree.insert_node(6)
tree.insert_node(12)
tree.insert_node(4)
tree.insert_node(3)

tree.show_me()
