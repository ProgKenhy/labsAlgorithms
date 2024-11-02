from random import randint
from timeit import timeit


def radix_sort(arr):
    # находим размер самого длинного числа
    max_digits = max([len(str(x)) for x in arr])

    # указываем систему счисления
    base = 10

    # создаём промежуточный двойной массив из base элементов
    bins = [[] for _ in range(base)]

    # перебираем все разряды начиная с нулевого
    for i in range(max_digits):
        # для удобства выведем текущий номер разряда
        # print('✅ Номер разряда → ' + str(i))
        # перебираем все элементы в массиве
        for x in arr:
            # получаем цифру, стоящую в текущем разряде, в каждом числе массива
            digit = (x // base ** i) % base
            # отправляем число в ячейку, номер которой совпадает с цифрой в разряде
            bins[digit].append(x)
        # собираем в исходный массив все ненулевые значения из полученного массива
        arr = [x for queue in bins for x in queue]
        # print(arr)
        # print(bins)

        # очищаем промежуточный массив
        bins = [[] for _ in range(base)]

    return arr


def test_large_quick_sort():
    large_array = array.copy()
    radix_sort(large_array)
    # large_array.sort()


array = [randint(0, 100000000) for _ in range(1000000)]

execution_time = timeit(test_large_quick_sort, number=3)
print(f"Среднее время выполнения на массиве из 1,000,000 элементов: {execution_time / 3:.6f} секунд")

array = [10, 1, 3, 6, 5, 99, 0, 13, 12]
print(radix_sort(array))
