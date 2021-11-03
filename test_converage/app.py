
def fibonacci(num):
    if num <= 1:
        return 1

    else:
        return fibonacci(num - 2) + fibonacci(num - 1)


def factorial(num):
    if num == 0:
        return 1

    else:
        return num * factorial(num - 1)
