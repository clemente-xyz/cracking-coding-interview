# Linear sort pseudo-algorithm:

'''
linear_sort(arr):
    if lenght(array)=1, then:
        return arr
    
    else, then:
        for i from 0 to lenght(arr)-1, do: 
            for j from i+1 to lenght(arr)-1, do:
                if arr[j]<=arr[i], then:
                    swap(arr[i], arr[j])
            
'''

# Linear sort algorithm:


def linear_sort(arr):  # O(n^2)
    if len(arr) == 1:
        return arr

    else:
        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j] <= arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]

        return arr


# Quick sort pseudo-algorithm:


'''
quick_sort(arr):
    if length(arr)=1, then:
        return arr
    
    else, then:
        set pivot as arr[lenght(arr)-1]
        set first_bigger_idx as 0
        
        for i from 0 to length(arr)-1, do:
            if arr[i]<=pivot, then:
                swap(arr[first_bigger_idx], arr[i])
                increment first_bigger_idx in 1
        
        swap(arr[first_bigger_idx], arr[lenght(arr)-1])
        
        set left_side_sorted as quick_sort(arr[0..pivot-1])
        set right_side_sorted as quick_sort(arr[pivot..arr[lenght(arr)]])

        return left_side_sorted+right_side_sorted
    
'''

# Quick sort algorithm:


def quick_sort(arr):  # O(log(n))
    if len(arr) == 1 or len(arr) == 0:
        return arr

    else:
        pivot = arr[-1]
        j = 0

        for i in range(0, len(arr)):
            if arr[i] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1

        arr[j], arr[-1] = arr[-1], arr[j]

        left_sorted_arr = quick_sort(arr[:j])
        right_sorted_arr = quick_sort(arr[j+1:])
        left_sorted_arr.append(arr[j])

        return left_sorted_arr + right_sorted_arr


arr = [9, 0, 1, 12, 0, 3]
print(quick_sort(arr))
