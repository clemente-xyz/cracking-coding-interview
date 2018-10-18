# Problem 1:
'''
Consider an array of n distinct integers, wich can be swap any two elements 
any number of times. An array is beautiful if the sum of |arr[i]-arr[i-1]| 
among 0<i<n is minimal.
Given the array arr, determine and return the minimum number of swaps that 
should be performed in order to make the array beautiful.
'''


def beutify_arr(arr):
    if len(arr) == 1 or len(arr) == 0:
        return 0

    else:
        sorted_arr = sorted(arr)
        swaps = 0

        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                arr[i], arr[arr.index(sorted_arr[i])
                            ] = arr[arr.index(sorted_arr[i])], arr[i]
                swaps += 1
                print(arr)

        return swaps


arr = [2, 5, 3, 1]

print(beutify_arr(arr))
