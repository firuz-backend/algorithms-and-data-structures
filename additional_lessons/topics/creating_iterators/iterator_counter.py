class Counter:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low > self.high:
            raise StopIteration

        self.low += 1
        return self.low - 1


# создаем итератор Counter, передавая значения low=3, high=10
counter1 = Counter(3, 10)

# iterator = iter(counter1)
print(next(counter1))
print(next(counter1))
