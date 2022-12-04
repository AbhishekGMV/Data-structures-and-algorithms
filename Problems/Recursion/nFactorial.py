def factorial(n):
    if n < 2:
        return 1

    n1 = n * factorial(n-1)
    return n1


factorial(5)
