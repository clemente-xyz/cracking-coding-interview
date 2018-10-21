def merge_inorder(left_middle_arr, right_middle_arr):
    ordered_merged_arr = []
    i, j = 0, 0

    while i < len(left_middle_arr) and j < len(right_middle_arr):
        if left_middle_arr[i] <= right_middle_arr[j]:
            ordered_merged_arr.append(left_middle_arr[i])
            print(i)
            print(j)
            i += 1

        else:
            ordered_merged_arr.append(right_middle_arr[j])
            print(i)
            print(j)
            j += 1

    if i == len(left_middle_arr):
        ordered_merged_arr.extend(right_middle_arr[j:])

    else:
        ordered_merged_arr.extend(left_middle_arr[i:])

    return ordered_merged_arr
