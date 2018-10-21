def quicksort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    pivot = arr[-1]
    j = 0

    for i in range(0, len(arr)):
        if arr[i] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    arr[j], arr[-1] = arr[-1], arr[j]

    left_arr_side = quicksort(arr[:j])
    right_arr_side = quicksort(arr[j+1:])

    return left_arr_side + [arr[j]] + right_arr_side


print(quicksort([3, 8, 6, 7, 3, 1, 0]))
