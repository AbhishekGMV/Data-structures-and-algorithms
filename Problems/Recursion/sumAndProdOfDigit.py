def sum(n):

    if n % 10 == n:
        return n

    return (n % 10) + sum(n//10)


def prod(n):

    if n % 10 == n:
        return n

    return (n % 10) * prod(n//10)


print(sum(12345))
print(prod(512))
