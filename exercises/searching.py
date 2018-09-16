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
Given a matrix in which each row and each column is sorted, write a method to find an element in it.
Assumptions:
- Rows are sorted left to right in ascending order Columns are sorted top to bottom in ascending order
- Matrix is of size MxN
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
target = 11

print(binary_search_in_matrix(matrix, target))
