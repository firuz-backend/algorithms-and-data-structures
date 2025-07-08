def simple_sequence():
    num = 1
    while True:
        for _ in range(num):
            yield num
        num += 1
