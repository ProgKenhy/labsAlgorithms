import string
import re


class Parser:
    def __init__(self, file_path):
        self.text = None
        self.file_path = file_path
        self.read_file()
        self.array = None
        self.text_to_words_array()


    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.text = f.read()

    def text_cleaner(self):
        self.text = re.sub(rf"[{string.punctuation}—]", "", self.text)
        self.text = self.text.lower()

    def text_to_words_array(self):
        self.text_cleaner()
        self.array = self.text.split()

