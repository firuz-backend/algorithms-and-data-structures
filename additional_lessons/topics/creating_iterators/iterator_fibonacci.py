class Fibonacci:
    def __init__(self):
        self.num = 1
        self.next = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.next, self.num = self.num, self.next + self.num
        return self.next
