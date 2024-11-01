def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


array = [10, 3, 5, 7, 1, 2, 76, 1, 5, 7, 1, 3, 6, 8, 89, 45, 3, 2, 56, 87, 9, 9, 7, 123, 5, 34, 32, 3, 6, 8]
print(selection_sort(array))
