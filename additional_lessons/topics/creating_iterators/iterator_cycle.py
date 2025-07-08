class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.iterable[self.index]
        self.index += 1

        if self.index == len(self.iterable):
            self.index = 0

        return res


cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))
