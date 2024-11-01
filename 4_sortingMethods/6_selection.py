import random
import timeit


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def test_large_quick_sort():
    large_array = array.copy()
    selection_sort(large_array)


array = [random.randint(0, 100000000) for _ in range(1000)]

execution_time = timeit.timeit(test_large_quick_sort, number=1)
print(f"Среднее время выполнения на массиве из 1,000,000 элементов: {execution_time / 1:.6f} секунд")

array = [10, 1, 3, 6, -5, 99, 0, 13, 12]
selection_sort(array)
print(array)
