class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.iterator = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.iterator)
        return key, self.data[key]
