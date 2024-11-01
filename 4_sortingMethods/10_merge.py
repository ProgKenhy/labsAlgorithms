def merge(left, right):
    sorted_list = []
    l_index = r_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            sorted_list.append(left[l_index])
            l_index += 1
        else:
            sorted_list.append(right[r_index])
            r_index += 1

    sorted_list.extend(left[l_index:])
    sorted_list.extend(right[r_index:])

    print(sorted_list, 'merge')
    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    print(arr, '"merge sort"')

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


array = [10, 3, 5, 7, 1, 2, 745, 3, 2, 56, 87, 9, 9, 7, 123, 5, 34, 32, 3, 6, 8]
print(merge_sort(array))
