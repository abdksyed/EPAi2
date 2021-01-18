# KINDLY GO THROUGH TEST FILE TO UNDERSTAND
from typing import List
import time
import gc
import sys

# Here in this code we will be leaking memory because we are creating cyclic reference.
# Find that we are indeed making cyclic references.
# Eventually memory will be released, but that is currently not happening immediately.
# We have added a function called "clear_memory" but it is not able to do it's job. Fix it.
# Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that
# this code is sub-optimal.


class Something(object):
    '''A dummy Class which is used to create Cyclic References'''

    def __init__(self):
        super().__init__()
        self.something_new = None

    def __repr__(self):
        return f'Something at {id(self)} which has something_new at {id(self.something_new)}.'


class SomethingNew(object):
    '''Anothe Dummy Class which is used to create Cyclic Reference.
        Arguments:
        i -> int -> default= 0. Just a variable.
        Something -> Class Object -> default= None'''

    def __init__(self, i: int = 0, something: Something = None):
        super().__init__()
        self.i = i
        self.something = something

    def __repr__(self):
        return f'SomethingNew at {id(self)} which has only something at {id(self.something)}.'


def add_something(collection: List[Something], i: int):
    '''A Function which takes a list and int as input.
        Creates Cyclic References using Two Class Objects and append
        it to the main list.'''

    something = Something()
    something.something_new = SomethingNew(i, something)
    collection.append(something)


def reserved_function():
    '''To be used in future if required'''
    pass


def clear_memory(collection: List[Something]):
    '''A function which take a list as input and performs clearing
        the list and clearing all cyclic references using garbage collector.'''

    collection.clear()
    gc.collect()


def critical_function():
    '''This Function will runs the above *add_something* fucntion for 1024*128(131,071) times 
        and create tons of cyclic references loading the memory.
        At last calling clear_memory to clean up the memory.'''

    collection = list()
    for i in range(1, 1024 * 128):
        add_something(collection, i)
    clear_memory(collection)


# Here we are suboptimally testing whether two strings are exactly same or not
# After that we are trying to see if we have a particular character in that string or not
# Currently the code is suboptimal. Write it in such a way that it takes 1/10 the current time

# DO NOT CHANGE THIS PROGRAM
def compare_strings_old(n):
    '''The function has two very long strings with whitesapces, so it is not interned.
        The function take a number *n* and checks whether the two strings are exact same
        or not for n times. (Here exactly same refers to same value and in same location).
        And also, the second part in the code check for the letter 'd' in the list of 
        characters of the string for n times.'''

    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass

# YOU NEED TO CHANGE THIS PROGRAM


def compare_strings_new(n):
    '''The function has two very long strings with whitesapces, so it is not interned.
        But the string is explicitly interned using sys.inten.
        The function take a number *n* and checks whether the two strings are exact same
        or not for n times. (Here exactly same refers to same value and in same location).
        And also, the second part in the code check for the letter 'd' in the list of 
        characters of the string for n times.'''

    a = sys.intern('a long string that is not intered') * 200
    b = sys.intern('a long string that is not intered') * 200
    for _ in range(n):
        if a is b:
            pass
    char_set = frozenset(a)
    for char in char_set:
        if 'd' is char:
            pass
