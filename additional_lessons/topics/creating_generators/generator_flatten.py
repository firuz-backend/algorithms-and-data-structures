def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def flatten2(nested_list):
    for x in nested_list:
        yield from flatten(x) if isinstance(x, list) else (x,)


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)
