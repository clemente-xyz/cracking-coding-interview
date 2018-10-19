from helpers import initialize_binary_tree, find_binary_tree_height

# Problem 1
'''
Given a binary tree, check if it's balanced or not.

Consider that a binary tree is balanced if for each node in the tree, 
the difference between the height of the right subtree and the left 
subtree is at most one.
'''

'''
is_balanced(node):
    if node is none, then:
        tree is balanced
    
    set left_height as get_height(node's left child)
    set right_height as get_height(node's right child)

    set heights_diff as abs(left_height - right_height)

    if heights_diff > 1, then:
        tree is not balanced
    
    is_balanced(node's left child)
    is_balanced(node's right child)

    tree is balanced 


'''


def is_balanced_index():
    binary_tree = initialize_binary_tree(5, [0, 1, 2, 3, 4, 5, 6, 7], [(
        2, 5, "left"), (6, 5, "right"), (1, 2, "left"), (3, 2, "right"), (4, 1, "left")])

    root_node = binary_tree.root_node

    return is_balanced(root_node)


def is_balanced(node):
    if node == None:
        return True

    left_height = find_binary_tree_height(node.left_child)
    right_height = find_binary_tree_height(node.right_child)

    heights_diff = abs(left_height - right_height)

    if heights_diff > 1:
        return False

    is_balanced(node.left_child)
    is_balanced(node.right_child)

    return True


print(is_balanced_index())
