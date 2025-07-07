class Factorials:
    def __init__(self):
        self.index = 1
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value *= self.index
        self.index += 1

        return self.value


infinite_factorials = Factorials()

for index, num in enumerate(infinite_factorials, 1):
    if index <= 10:
        print(f'Факториал числа {index} равен {num}')
    else:
        break
