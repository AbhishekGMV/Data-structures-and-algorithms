def nToOne(n):
    if n == 0:
        return 0

    print(n)
    nToOne(n-1)


def oneToN(n):
    if n == 0:
        return 0

    oneToN(n-1)
    print(n)


def oneToNNToOne(n):
    if n == 0:
        return 0
    print(n)
    oneToNNToOne(n-1)
    print(n)


oneToNNToOne(5)
