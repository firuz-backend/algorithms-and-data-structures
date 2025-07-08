def generate_ints(n):
    for num in range(n):
        yield num


generator1 = generate_ints(5)
for num in generator1:
    print(num)


def generate_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


gen = generate_AB()

for i in gen:
    print('---->', i)


print('NEWWWWW')


for i in gen:
    print('---->', i)
