import operator
from functools import reduce
from itertools import combinations

'''
 l = lista cu valori
 func = o metoda care o aplica la toate sublistele si care returneaza True / False pentru o anumita sublista

 l = [1, 2, 3]
 sublists = [ [ 1 ], [ 1, 2 ], [ 2, 3 ], [ 1, 2, 3 ] ]
 True <- func [1],
False <- func [ 1,2],
 True <- func [2, 3]
 pentru toate sublistele care returneaza True asta inseamna ca sunt subliste valide / de luat in considerare ca si un
 raspuns
 cu toate sublistele valide, se face un max dupa lungimea lor
'''
def process_simple_sublists(l, func):
    return max(filter(func, get_sublists(l)), key=len)


def process_interdependent_sublists(l, process_func):
    '''
    pentru suma/produs:
    l = [1, 2, 3]
     mapper [ [ suma/produs(sublistei), sublista ], [ suma/produs(sublistei), sublista ] etc. ]
    '''
    mapper = list(map(lambda x: [process_func(x), x], get_sublists(l)))

    '''
    verifica care este suma / produs maxima a elementelor
    '''
    max_val = max(mapper, key=lambda x: x[0])[0]

    '''
    returneaza cea mai lunga sublista care are suma / produs maxima
    '''
    return max([i[1] for i in mapper if i[0] == max_val], key=len)

'''
ia o lista l ca si input si genereaza toate sublistele folosind conbinations din itertools (modul)

poate fi inlocuit cu:
sublists = []
for i in range(len(lst)):
    for j in range(i, len(lst)):
        sublists.append(lst[i:j+1])

'''
def get_sublists(l):
    for start, end in combinations(range(len(l)), 2):
        yield l[start:end + 1]
    # sublists = []
    # for i in range(len(l)):
    #     for j in range(i, len(l)):
    #         sublists.append(l[i:j+1])
    # return sublists

'''
se aplica pe o sublista (care ii tot o lista)
si returneaza True / False in functie de caz - daca lista contine doar elemenente disticte
'''
def is_list_distinctive(l):
    '''
    set matematic - o multime cu elemente unice
    list poate contine duplicate, set-ul nu poate contine
    exemplu:
    l = [1,2, 3, 2, 3, 1, 2, 3, 4]
    set(l) = [1, 2, 3, 4]
     '''
    return len(l) == len(set(l))

'''
daca o sublista contine doar elemente prime
'''
def is_list_prime(l):
    '''
        [   1,    2,    3   ]
    all([ True,  True, True ]) -> True else False
    all - functie de la Python - returneaza True daca conditia din ea este True
    '''
    return all([is_prime(i) for i in l])


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def has_three_distinct_values(l):
    return len(set(l)) == 3


def has_gcd_different_from_one(l):
    '''
    reduce - metoda de la Python
     list - [1, 2, 3]
     gcd (x, y)
     reduce(gcd, list) - gcd(1, gcd(2, 3) )
     gcd(1, <- 1
        (gcd (2, 3) <- 1
     )
    '''
    return reduce(lambda x, y: gcd(x, y), l) > 1


def gcd(x, y):
    return x if not y else gcd(y, x % y)


def has_same_parity_for_all_elements(l):
    '''
        i % 2 == 1 - impar
        i % 2 == 0 - par
    '''
    return all(i % 2 == 1 for i in l) or all(i % 2 == 0 for i in l)


def is_hill(l):
    '''
    [1, 2, 3, 4, 3, 2, 1]
    '''
    '''
    m1 - indexul de urcare
    m2 - indexul de coborare
    '''
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


def product(l):
    return reduce(operator.mul, l, 1)


def min_elem_positive(l):
    return min(l) >= 0


def max_elem_10(l):
    return max(l) == 10


def is_palindrome(numb):
    return str(numb) == str(numb)[::-1]


def is_all_sublist_palindrome(l):
    return all(is_palindrome(i) for i in l)


def ends_in_6(l):
    return all(str(i)[-1] == '6' for i in l)

