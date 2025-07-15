def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


def chain2(*iterables):
    for it in iterables:
        yield from it
