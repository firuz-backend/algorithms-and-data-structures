def filterfalse(func, iterable):
    if func is None:
        func = bool

    return filter(lambda x: not func(x), iterable)


objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))
