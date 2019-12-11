__author__ = 'huzef'
def factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if not n % i)))