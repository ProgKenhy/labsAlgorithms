import heapq


# разделение исходных данных на отсортированные подмассивы
def split_and_sort(data, chunk_size):
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunk = sorted(data[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


# слияние отсортированных подмассивов в один
def merge_sorted_chunks(chunks):
    result = []
    print(*chunks)
    for chunk in heapq.merge(*chunks):
        result.append(chunk)
    return result


# внешняя многофазная сортировка
def external_sort(data, chunk_size):
    sorted_chunks = split_and_sort(data, chunk_size)
    return merge_sorted_chunks(sorted_chunks)


data = [20, 5, 12, 30, 25, 1, 17, 19, 22, 7, 15, 3]
chunk_size = 4  # размер блока, помещающегося в память

sorted_data = external_sort(data, chunk_size)
print(sorted_data)
