def filter_names(names, ignore_char, max_names):
    only_names = filter(lambda x: x.isalpha(), names)
    cleared_names = (
        name for name in only_names
        if not name.lower().startswith(ignore_char.lower()))
    counter = 0
    for i in cleared_names:
        if counter == max_names:
            break
        yield i
        counter += 1


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))
