from random import randint
from timeit import timeit


def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    is_sorted = False

    while not is_sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            is_sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                is_sorted = False
            i += 1


def test_large_quick_sort():
    large_array = array.copy()
    comb_sort(large_array)


array = [randint(0, 100000000) for _ in range(1000000)]
execution_time = timeit(test_large_quick_sort, number=1)
print(f"Среднее время выполнения на массиве из 1,000,000 элементов: {execution_time / 1:.6f} секунд")

array = [10, 1, 3, 6, -5, 99, 0, 13, 12]
comb_sort(array)
print(array)
