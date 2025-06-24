numbers = [1, 2, 3]
name = 'python'

for num in numbers:        # итерируем по списку, перебирая каждый элемент
    print(num)

for c in name:             # итерируем по строке, перебирая каждый символ
    print(c)

print(2 in numbers)        # неявное итерирование по списку
print('A' in name)         # неявное итерирование по строке
print(*numbers)            # неявное итерирование по списку при распаковке


iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

numbers = range(0, 5, 2)
print(numbers)
