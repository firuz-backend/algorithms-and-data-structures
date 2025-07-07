class Square:
    def __init__(self, n):
        self.n = iter(range(1, n + 1))

    def __iter__(self):
        return self

    def __next__(self):
        num = next(self.n)
        return num ** 2


squares = Square(10)

print(list(squares))
