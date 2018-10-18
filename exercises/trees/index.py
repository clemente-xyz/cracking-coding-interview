from helpers import initialize_binary_tree

# Problem 1
'''
Given a binary tree, check if it's balanced or not.

Consider that a binary tree is balanced if for each node in the tree, 
the difference between the height of the right subtree and the left 
subtree is at most one.
'''


def is_balanced():
    binary_tree = initialize_binary_tree(5, [0, 1, 2, 3, 4, 5, 6, 7], [
        (2, 5, "left"), (6, 5, "right")])

    binary_tree.show_me_in_bfs()


is_balanced()
