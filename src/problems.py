from functools import reduce
from itertools import combinations


def process_simple_sublists(l, func):
    return max(filter(func, get_sublists(l)), key=len)


def process_interdependend_sublists(l, process_func):
    return max(map(lambda x: [process_func(x), x], get_sublists(l)), key=lambda x: x[0])[1]


def get_sublists(l):
    for start, end in combinations(range(len(l)), 2):
        yield l[start:end + 1]


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
    return reduce(lambda x, y: gcd(x, y), l) > 1


def gcd(x, y):
    return x if not y else gcd(y, x % y)


def has_same_parity_for_all_elements(l):
    return all(i % 2 == 1 for i in l) or all(i % 2 == 0 for i in l)


def is_hill(l):
    m1, m2 = 0, 0
    for i in range(1, len(l)):
        if l[i - 1] < l[i] and m2 == 0:
            m1 = i
        elif l[i - 1] > l[i] and m1 != 0:
            m2 = i
        else:
            return False
    return m1 < m2


def has_difference_between_elements_of_a_range(l):
    return all(-5 <= i - j <= 5 for i, j in zip(l, l[1:]))


def items_in_interval(l):
    return all(0 <= i <= 10 for i in l)


def lcd(x, y):
    return x * y // gcd(x, y)


def has_lcd_smaller_than_100(l):
    return reduce(lambda x, y: lcd(x, y), l) <= 100



