from functools import reduce, partial
import math
import random

fib_prestored = [1, 1]
while fib_prestored[-1] < 10000:
    fib_prestored.append(fib_prestored[-1] + fib_prestored[-2])


def check_fib(check_list: list) -> list:
    '''The Function takes a list of numbers, and check if the individual numbers
    in the list is a Fibonacci number (upto around 10000), and returns the list
    of all Fibonacci Numbers present in the Input List.
    Arguments:
    Input: List of Numbers to be check.
    Return: List of Fibonacci Numbers(upto 10000) (if any) in Input List
    '''
    if not isinstance(check_list, list):
        raise TypeError('check_list must be of type <list>')
    for val in check_list:
        if val < 0 or val > 10000:
            raise ValueError('The values in list must be in between 0 and 10000')
    return list(filter(lambda x: x in fib_prestored, check_list))


add_even_odd = lambda l1,l2: list(map(
    lambda a: a[0]+a[1], list(filter(lambda x:  x[0] % 2 == 0 and x[1] % 2 != 0, zip(l1, l2)))))
add_even_odd_direct = lambda l1,l2: [x+y for x,
                       y in zip(l1, l2) if x % 2 == 0 and y % 2 != 0]


strip_vowel = lambda inp_string: ''.join(
    [x for x in inp_string if x not in ['a', 'e', 'i', 'o', 'u']])


relu = lambda neurons: [x if x >= 0 else 0 for x in neurons]


sigmoid = lambda neurons: [1/(1+math.exp(x)) for x in neurons]


shifted_string = lambda small_char_string: ''.join([chr({118: 92, 119: 93, 120: 94, 121: 95, 122: 96}.get(ord(x), ord(x))+5)
                          for x in small_char_string])



with open("swear_words.txt", "r") as f:
    swear_words_master = f.read().split()
    
swear_word_list = lambda inp_text: [x for x in inp_text.split() if x.lower()
                   in swear_words_master]


add_even_odd_reduce = lambda num_list: reduce(
    lambda x, y: x+y, filter(lambda x: x % 2 == 0, num_list))


big_char = lambda small_char_string: reduce(lambda x, y: x if ord(x) > ord(y) else y, small_char_string)


add_3rd = lambda num_list: reduce(lambda x, y: x+y, [num_list[i-1]
                                    for i in range(1, len(num_list)+1) if i % 3 == 0])



num_plates = [('KA'+str(random.randint(10, 99))+chr(random.randint(65, 90)) +
               chr(random.randint(65, 90))+str(random.randint(1000, 9999))) for _ in range(15)]


def variable_num_plate(state: str, two_d: int, two_alp: str, four_d: int) -> str:
    '''The Function generates a number plate.
    Inputs:
    state: the first characters of number plate.
    two_d: the 3rd and 4th character which is a number from 10-99(2 digit)
    two_alp: the characters, ranging from (AA to ZZ)
    four_d: the final four characters which is a number from 1000 - 9999
    Returns:
    A Number plate code.
    '''
    if not isinstance(state, str):
        raise TypeError('The State should be string, like DL/KA etc')
    if isinstance(two_d, int):
        two_d = str(two_d)
    if isinstance(four_d, int):
        four_d = str(four_d)
    return state + two_d + two_alp + four_d


part_num_plate = partial(variable_num_plate, two_d=47,
                         two_alp='AK', four_d=9999)