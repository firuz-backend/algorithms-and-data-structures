from math import sqrt


def is_prime(number):
    if number < 2:
        return False

    for j in range(3, int(sqrt(number)) + 1, 2):
        if number % j == 0:
            return False
    else:
        return True


def primes(left, right):

    if 2 in range(left, right + 1):
        yield 2

    left = left + 1 if left % 2 == 0 else left

    for i in range(left, right + 1, 2):
        if is_prime(i):
            yield i


generator = primes(1, 30)

print(*generator)
