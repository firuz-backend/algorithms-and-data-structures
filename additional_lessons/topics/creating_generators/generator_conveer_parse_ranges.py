def parse_ranges(ranges):
    ranges = ranges.split(',')
    tuple_ranges = (list(map(int, ran.split('-'))) for ran in ranges)
    ranged_number = (i for ranged in list(tuple_ranges) for i in range(
        ranged[0], ranged[1] + 1))
    return ranged_number


print(*parse_ranges('1-10,2-10'))
