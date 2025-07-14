def primes(left, right):
    if left == 0:
        left += 1
    if 2 in range(left, right + 1):
        yield 2
    left = left + 1 if left % 2 == 0 else left

    for i in range(left, right + 1, 2):
        if i == 0:
            continue
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
        if counter != 2:
            continue
        yield i
