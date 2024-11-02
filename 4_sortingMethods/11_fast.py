from random import randint
from timeit import timeit


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if j <= i:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):
    def _quick_sort(arr, low, high):
        if low < high:
            split_index = partition(arr, low, high)
            _quick_sort(arr, low, split_index)
            _quick_sort(arr, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)


array = [randint(0, 100000000) for _ in range(1000000)]


def test_large_quick_sort():
    large_array = array.copy()
    quick_sort(large_array)


execution_time = timeit(test_large_quick_sort, number=3)
print(f"Среднее время выполнения на массиве из 1,000,000 элементов: {execution_time / 3:.6f} секунд")

array = [10, 1, 3, 6, -5, 99, 0, 13, 12]
quick_sort(array)
print(array)