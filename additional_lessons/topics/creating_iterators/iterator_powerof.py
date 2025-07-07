class PowerOf:
    def __init__(self, number):
        self.number = number
        self.index = -1
        self.cache = {0: 1}

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == 0:
            return self.cache[self.index]
        res = self.cache[self.index] = self.cache[self.index - 1] * self.number

        return res


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
