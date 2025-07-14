def reverse(sequence):
    for i in range(len(sequence) - 1, -1, -1):
        yield sequence[i]


print(*reverse([1, 2, 3, 4, 5]))
