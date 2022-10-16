import datetime


def decorator(function):
    def inner(*args):
        now = datetime.datetime.now()
        print(f'fuction that currently execution {function.__name__}')
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        return function(*args)

    return inner


@decorator
def sum_two_number(a, b):
    x = a + b
    return x


@decorator
def sub_two_number(a, b):
    if a > b:
        return a - b
    return b - a


print(sum_two_number(5, 5))
print(sub_two_number(5, 2))
