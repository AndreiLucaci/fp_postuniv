''' are rezolvarile la probleme '''
from problems import *


def show_menu(l):
    print_menu()
    get_menu_answer(l)


def print_menu():
    print('''
1. Distinct sublists
2. Prime elements
3. Exactly 3 distinct sublists
4. GCD of elements is greater than 1
5. All elements have the same parity
6. Is hill
7. Difference
8. Interval
9. LCD smaller than 100
10. Max sum of elements
11. Max product of elements
12. Min element to be positive
13. Max element to be 10
14. All elements are palindrome
15. All elements end in '6'
q to exit
m to show the menu
    ''')


def get_menu_answer(l):
    while True:
        answer = input('~: ')
        if answer == 'q': break
        elif answer == 'm': print_menu()
        elif answer == '1':
            ''' l[:] - creaza o copie la lista '''
            print(process_simple_sublists(l[:], is_list_distinctive))
        elif answer == '2':
            print(process_simple_sublists(l[:], is_list_prime))
        elif answer == '3':
            print(process_simple_sublists(l[:], has_three_distinct_values))
        elif answer == '4':
            print(process_simple_sublists(l[:], has_gcd_different_from_one))
        elif answer == '5':
            print(process_simple_sublists(l[:], has_same_parity_for_all_elements))
        elif answer == '6':
            print(process_simple_sublists(l[:], is_hill))
        elif answer == '7':
            print(process_simple_sublists(l[:], has_difference_between_elements_of_a_range))
        elif answer == '8':
            print(process_simple_sublists(l[:], items_in_interval))
        elif answer == '9':
            print(process_simple_sublists(l[:], has_lcd_smaller_than_100))
        elif answer == '10':
            print(process_interdependent_sublists(l[:], sum))
        elif answer == '11':
            print(process_interdependent_sublists(l[:], product))
        elif answer == '12':
            print(process_simple_sublists(l[:], min_elem_positive))
        elif answer == '13':
            print(process_simple_sublists(l[:], max_elem_10))
        elif answer == '14':
            print(process_simple_sublists(l[:], is_all_sublist_palindrome))
        elif answer == '15':
            print(process_simple_sublists(l[:], ends_in_6))
        else:
            print("Invalid command: " + answer + " is not recognized as a valid input.")


def get_read_list_answer():
    print('Read list: ')
    # this is the raw string read from the keyboard
    raw_list = input('Comma separated values: ')
    # we split the values by the comma
    splitted_values = raw_list.split(',')
    # initialize a new empty list
    l = []
    # iterate over the splitted values
    for i in splitted_values:
        # strip the space characters from the value e.g. " 1 " -> "1"
        trimmed = i.strip()
        # convert the value to an int
        try:
            int_val = int(trimmed)
            # add the int value to the list
            l.append(int_val)
        except ValueError:
            print('Invalid string provided: ' + i + ' is not a number.')
    return l
