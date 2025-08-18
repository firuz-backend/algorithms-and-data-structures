from datetime import date, timedelta


def years_days(year):
    current = date(year=year, month=1, day=1)
    while current.year == year:
        yield current
        current = current + timedelta(days=1)


dates = years_days(2022)

for i in range(100):
    print(next(dates))
