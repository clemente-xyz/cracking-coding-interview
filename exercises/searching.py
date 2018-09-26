# Problem 1:
'''
Given a sorted array of n integers that has been rotated an unknown number of
times, give an O(log n) algorithm that finds an element in the array. You may assume
that the array was originally sorted in increasing order.
'''


def search(array):
    low = 0
    high = len(array) - 1
    mid = int((low + high)/2)


# Problem 2:
'''
Given a sorted array of strings which is interspersed with empty strings, write a method
to find the location of a given string.
Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] will return 4
Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return -1
'''


def search_str_array(array, target):  # O(n^2)
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((low+high)/2)
        if array[mid] == target:
            return mid
        elif array[mid] == "":
            verificator = False
            for i in range(mid, high):
                if array[i] != "":
                    if array[i] > target:
                        high = mid - 1
                    elif array[i] == target:
                        return i
                    elif array[i] < target:
                        low = i
                    verificator = True
            if verificator == False:
                high = mid - 1
        elif array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
    return False


# Problem 3:
'''
Given a matrix in which each row and each column is sorted, write a method to find an element in it.
Assumptions:
- Rows are sorted left to right in ascending order Columns are sorted top to bottom in ascending order
- Matrix is of size MxN
'''


def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int(0.5*(low + high))

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            low = mid + 1

        elif array[mid] > target:
            high = mid - 1

    return False


def binary_search_in_matrix(matrix, target):
    low = 0
    high = len(matrix) - 1

    while low <= high:
        mid = int(0.5*(low + high))
        test = binary_search(matrix[mid], target)

        if test == False:
            low_mid = 0
            high_mid = len(matrix[mid]) - 1

            if matrix[mid][low_mid] < target:
                low = mid + 1

            elif matrix[mid][high_mid] > target:
                high = mid - 1

        else:
            return (test, mid)

    return False


# Problem 4:
'''
For the purposes of this challenge, we define a binary tree to be a binary search tree with the 
following ordering requirements:

1. The  value of every node in a node's left subtree is less than the data value of that node.
2. The  value of every node in a node's right subtree is greater than the data value of that node.

Given the root node of a binary tree, can you determine if it's also a binary search tree?

Input Format - A pointer to the root of a binary tree.

Output Format - A boolean denoting whether or not the binary tree is a binary search tree.

Constraints - 0 <= data <= 10^4

'''


def check_binary_search_tree_(root):
    return _check_binary_search_tree(root, -1, 10001)


def _check_binary_search_tree(node, min, max):
    if node is None:
        return True
    else:
        if node.data >= max or node.data <= min:
            return False

        return _check_binary_search_tree(node.left, min, node.data) and _check_binary_search_tree(node.right, node.data, max)


# Problem 5:
'''
Anna loves graph theory! She has a tree where each vertex is numbered from 1 to n, and each contains a 
data value. The sum of a tree is the sum of all its nodes' data values. If she cuts an edge in her tree, 
she forms two smaller trees. The difference between two trees is the absolute value between their sums.

Given a tree, determine which edge to cut so that the resulting trees have a minimal difference between 
them, then return that difference.

            100
             | (1,2)
            200
     (2,5) /   \ (2,3)
         100   100
  (4,5) /   \ (5,6)
      500   600
         
'''


# input: subtree / output: sum of subtree nodes
def find_and_sum_subtree_nodes(root_idx, edges, nodes, sum):
    for i in edges:
        if i[0] == root_idx or i[1] == root_idx:


def tree_min_diff_in_cut(nodes, edges):
    differences = []

    for e in edges:
        left_tree_sum = find_and_sum_subtree_nodes(e[0], edges, nodes)
        right_tree_sum = find_and_sum_subtree_nodes(e[1], edges, nodes)
        difference = abs(left_tree_sum-right_tree_sum)
        differences.append(difference)

    return min(differences)


nodes = [100, 200, 100, 500, 100, 600]
edges = [(1, 2), (2, 3), (2, 5), (4, 5), (5, 6)]

print(tree_min_diff_in_cut(nodes, edges))
