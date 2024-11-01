def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


array = [10, 3, 5, 7, 1, 2, 745, 3, 2, 56, 87, 9, 9, 7, 123, 5, 34, 32, 3, 6, 8]
print(insertionSort(array))
