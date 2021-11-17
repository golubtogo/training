__author__ = 'Nataliya'


from datetime import date
from datetime import timedelta


def percents(x, y):
    """What percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    return result


def print_percents(x, y):
    """Print what percentage of x is y"""
    p = percents(x, y)
    print(f"{y} is {p}% of x")


print_percents(100, 13)


def count_family_days():
    x = date.today()
    y = date(2005, 12, 12)
    delta = x - y
    print(delta.days)


print("3000 days from today will be " + str(date.today() + timedelta(days=3000)))
print("6000 days from 2005, 12, 12 will be " + str(date(2005, 12, 12) + timedelta(days=6000)))