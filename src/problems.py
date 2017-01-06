from functools import reduce


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


def has_gcd_different_from_one(l):
    gcd = lambda m, n: m if not n else gcd(n, m % n)
    return reduce(lambda x, y: gcd(x, y), l) > 1


def has_same_parity_for_all_elements(l):
    return all(i % 2 == 1 for i in l) or all(i % 2 == 0 for i in l)
