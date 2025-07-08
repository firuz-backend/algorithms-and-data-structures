def counter(low, high):
    for i in range(low, high + 1):
        yield i


counter1 = counter(3, 10)

for i in counter1:
    print(i)

counter2 = counter(100, 103)
print(next(counter2))
print(next(counter2))
