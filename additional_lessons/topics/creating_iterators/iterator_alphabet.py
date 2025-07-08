class Alphabet:
    const_alphabet = {
        'ru': list('абвгдежзийклмнопрстуфхцчшщъыьэюя'),
        'en': list('abcdefghijklmnopqrstuvwxyz')
    }

    def __init__(self, language):
        self.language = language
        self.alphabet = self.const_alphabet[self.language]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.alphabet):
            self.index = 0

        return self.alphabet[self.index]
