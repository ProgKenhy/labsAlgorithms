from text_parser_from_file import Parser


class HashTableWithOverlay:
    def __init__(self, file_path):
        self.array = Parser(file_path).array
        self.res = [[] for _ in range(len(self.array))]
        self.create_hash_table()
        self.write_to_file()

    def hash_key(self, word):
        key = 0
        for i in word:
            key += ord(i)
        return key % len(self.res)

    def create_hash_table(self):
        for word in self.array:
            self.insert(word)

    def insert(self, word):
        index = self.hash_key(word)
        if word in self.res[index]:
            return
        self.res[index].append(word)



    def search(self, word):
        index = self.hash_key(word)
        if word in self.res[index]:
            return index


    def delete(self, word):
        index = self.hash_key(word)
        if word in self.res[index]:
            self.res[index].remove(word)
            return True
        return False


    def print(self):
        self.create_hash_table()
        for key, value in enumerate(self.res):
            if value:
                print(f"Index {key}: {', '.join(value)}\n")

    def write_to_file(self):
        with open('output.txt', 'w', encoding='utf-8') as file:
            for key, value in enumerate(self.res):
                if value:
                    file.write(f"Index {key}: {', '.join(value)}\n")


if __name__ == "__main__":
    t = HashTableWithOverlay('input.txt')  # создаем хеш-таблицу из файла
    t.print()
    print("Поиск слова 'встают':", t.search('встают'))  # ищем слово 'встают'
    t.delete('встают')  # удаляем слово 'встают'
    print("Поиск после удаления слова 'встают':", t.search('встают'))  # проверяем, что слово удалено
    t.insert('тестслово')  # вставляем новое слово
    print("Поиск после вставки слова 'тестслово':", t.search('тестслово'))  # проверяем, что слово добавлено
    print(f"Содержимое индекса {t.search('тестслово')}: {t.res[t.search('тестслово')]}")  # проверяем содержимое конкретного индекса
    for i in range(3000):  # добавляем 3000 чисел в хеш-таблицу
        t.insert(str(i))
    t.print()  # выводим таблицу
    print("Поиск числа '2930':", t.search('2930'))  # ищем число '2930'
