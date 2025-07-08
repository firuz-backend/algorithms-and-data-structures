class Xrange:
    def __init__(self, start, end, step=1):
        self.end = end
        self.step = step
        self.start = start - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if (
            (self.start >= self.end and self.step > 0)
            or
            (self.start <= self.end and self.step < 0)
        ):
            raise StopIteration
        return self.start
