import pytest
import session7a
import os
import inspect
import re
from session7a import *
import test_session7a
import glob


README_CONTENT_CHECK_FOR = ['namedtuple', 'stock', 'exchange', 'index', 'profile', 'dictionary',
                            'Faker', 'immutable', 'runtime', 'age', 'location', 'blood']


# ----------------------------------------------Default checks Begin--------------------------------------------------#


README_CONTENT_CHECK_FOR = [
    'Named Tuples',
    'Tuples',
    'dictionary',
    'faker',
    'blood',
    'profiles',
    'decorator',
    'stock',
    'exchange',
    'companies',
    'high',
    'close',
    'open',
    'low'
]


CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile(
        "Session07_Tuples_SequenceTypes/README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("Session07_Tuples_SequenceTypes/README.md",
                  "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("Session07_Tuples_SequenceTypes/README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You haven't well described your README.md file"


def test_readme_file_for_formatting():
    f = open("Session07_Tuples_SequenceTypes/README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7a, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session7a, inspect.isfunction)
    assert len(functions) >= 10, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session7a, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session7a, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7a)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

# ----------------------------------------------Default checks End--------------------------------------------------#

# ----------------------------------------------Session 7a checks --------------------------------------------------#


def test_notebook_exists():
    assert glob.glob('*.ipynb')
