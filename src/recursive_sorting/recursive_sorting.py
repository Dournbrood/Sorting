# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if len(arrA) == 0 and len(arrB) == 0:
        return []
    elif len(arrA) == 0:
        return arrB
    elif len(arrB) == 0:
        return arrA

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # print(f"dummy array is {merged_arr}")

    i = 0
    j = 0
    k = 0
    while j < len(arrA) and k < len(arrB) and i < elements:
        # print(f"i is {i}\nj is {j}\nk is {k}")
        if arrA[j] <= arrB[k]:
            # print(
            #     f"arrA[{j}]: {arrA[j]} is less than or equal to arrB[{k}]: {arrB[k]}.")
            merged_arr[i] = arrA[j]
            i += 1
            j += 1
            # print(f"merged_arr is now: {merged_arr}")
        elif arrB[k] < arrA[j]:
            # print(
            #     f"arrB[{k}]: {arrB[k]} is less than arrA[{j}]: {arrA[j]}.")
            merged_arr[i] = arrB[k]
            i += 1
            k += 1
            # print(f"merged_arr is now: {merged_arr}")

    while i < elements:
        if j < len(arrA):
            merged_arr[i] = arrA[j]
            i += 1
            j += 1
        elif k < len(arrB):
            merged_arr[i] = arrB[k]
            i += 1
            k += 1

    # print(f"final merged array is {merged_arr}")
    return merged_arr


# [1, 3, 4, 2, 6, 7, 8]
merge([1], [6])
merge([1, 3, 7], [4, 2, 6, 8])
merge([1, 2, 2, 2, 3], [4, 5, 6, 7, 7, 7, 8])

print(merge([], [4, 5, 6, 7, 7, 7, 8]))
print(merge([1, 2, 2, 2, 3], []))
print(merge([], []))


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # print(f"arr is {arr}")
    if len(arr) <= 1:
        return arr

    subArr1 = arr[0:len(arr) // 2:1]
    subArr2 = arr[len(arr) // 2::1]

    # print(f"subArr1 is {subArr1}")
    # print(f"subArr1 is {subArr1}")

    return merge(merge_sort(subArr1), merge_sort(subArr2))


print(merge_sort([2, 1, 6, 7, 1, 5, 0, 4, 9]))
print(merge_sort([2, 643]))
print(merge_sort([3, 2, 2]))
print(merge_sort([3, 2]))
print(merge_sort([]))


# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
