def even_numbers(begin):
    begin += begin % 2
    while True:
        yield begin
        begin += 2


evens1 = even_numbers(10)

for index, num in enumerate(evens1):
    if index > 5:
        break
    print(num)

evens2 = even_numbers(101)

print(next(evens2))
print(next(evens2))
print(next(evens2))
print(next(evens2))
