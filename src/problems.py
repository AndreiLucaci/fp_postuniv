def process_simple_sublists(l, func):
    sublists = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            sublist = [l[k] for k in range(i, j + 1)]
            if func(sublist):
                sublists.append(sublist)
    return max(sublists, key=len)


def is_list_distinctive(l):
    return len(l) == len(set(l))


def is_list_prime(l):
    return all([is_prime(i) for i in l])


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def has_three_distinct_values(l):
    return len(l) == len(set(l)) == 3


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
