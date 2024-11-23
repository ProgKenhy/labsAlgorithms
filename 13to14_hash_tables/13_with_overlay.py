from text_parser_from_file import Parser


class HashTableWithOverlay:
    def __init__(self, input_file_path):
        self.array = Parser(input_file_path).array
        self.res = [None] * int(len(self.array) * 1.2)
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
        orig_index = index
        while self.res[index] is not None:
            if self.res[index] == word:
                return
            index = (index + 1) % len(self.res)
            if index == orig_index:
                self.resize()
                return self.insert(word)
        self.res[index] = word

    def resize(self):
        new_res = [None] * len(self.res) * 2
        old_res = self.res
        self.res = new_res
        for word in old_res:
            if word is not None and word != 'DELETED':
                self.insert(word)


    def search(self, word):
        index = self.hash_key(word)
        orig_index = index
        while self.res[index] is not None:
            if self.res[index] == word:
                return index
            index = (index + 1) % len(self.res)
            if index == orig_index:
                return None

    def delete(self, word):
        index = self.hash_key(word)
        orig_index = index
        while self.res[index] is not None:
            if self.res[index] == word:
                self.res[index] = 'DELETED'
                return True
            index = (index + 1) % len(self.res)
            if index == orig_index:
                return None

    def print(self):
        for key, value in enumerate(self.res):
            if value is not None:
                print(f"Index {key}: {value}")

    def write_to_file(self):
        with open('output.txt', 'w', encoding='utf-8') as file:
            for key, value in enumerate(self.res):
                if value is not None:
                    file.write(f"Index {key}: {value}\n")



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
    print("Поиск числа '2930':", t.search('2930'))  # ищем число '2953'
