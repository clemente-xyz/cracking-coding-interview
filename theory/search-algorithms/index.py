def linear_search(target, array):  # O(n)
    for i in array:
        if i == target:
            return array[i]
    return False


def binary_search(target, array):  # O(log[n])
    array.sort()  # Requirement of the algorithm
    low = 0
    high = len(array)-1

    while low <= high:
        mid = int((low+high)/2)
        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            high = mid-1
        else:
            low = mid+1

    return False


array = [0, 1, 2, 3, 4, 5, 6]
target = 0

print(binary_search(target, array))
