def string_wrapper(string, symbol):
    for i in string:
        yield symbol + i + symbol


string_wrapper1 = string_wrapper('beegeek', '~')

for i in string_wrapper1:
    print(i)
