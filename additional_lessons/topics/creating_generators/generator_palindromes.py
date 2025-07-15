def is_palindrom_str(length):
    if length == 1:
        yield from map(lambda i: str(i), range(0, 10))
    elif length == 2:
        yield from map(lambda i: str(i) + str(i), range(0, 10))
    elif length > 2:
        yield from (
            str(n) + i + str(n)
            for n in range(0, 10)
            for i in is_palindrom_str(length-2)
        )


def palindromes():
    L = 1
    while True:
        yield from (
            s
            for s in is_palindrom_str(L)
            if s[0] != '0'
        )
        L += 1


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)


generator = palindromes()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
