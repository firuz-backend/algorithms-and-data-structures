def alternating_sequence(count=None):
    n = 1
    while count is None or n <= count:
        yield n if n % 2 != 0 else n * -1
        n += 1


generator = alternating_sequence(10)

print(*generator)
