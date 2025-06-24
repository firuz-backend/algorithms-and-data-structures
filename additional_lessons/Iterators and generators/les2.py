lifo = [1, 2, 3]
print('__next__' in dir(lifo))


iterator = iter(lifo)
print('__next__' in dir(iterator))

for i in iterator:
    print(i)
    print('__next__' in dir(i))


iterator = reversed([1, 2, 3])
print('__next__' in dir(iterator))


gen = (i for i in range(5))
print(next(gen))
