import glob
import inspect
import os
import re
import pytest
import session7b_1
import session7b_2
import test_session7b

# ----------------------------------------------Default checks Begin--------------------------------------------------#

README_CONTENT_CHECK_FOR = ['namedtuple', 'stock', 'exchange', 'index', 'profile', 'dictionary',
                            'Faker', 'immutable', 'runtime', 'age', 'location', 'blood']

README_CONTENT_CHECK_FOR = [
    'sequence',
    'polygon',
    'getitem',
    'class',
    'regular',
    'strict',
    'max',
    'area'
]


CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile("Session07_Tuples_SequenceTypes/README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("Session07_Tuples_SequenceTypes/README.md", "r", encoding="utf8")
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


def test_function_count():
    functions = inspect.getmembers(test_session7b, inspect.isfunction)
    assert len(functions) >= 10, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session7b, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_notebook_exists():
    assert glob.glob('*.ipynb')
# ----------------------------------------------Default checks End--------------------------------------------------#


# ----------------------------------------------7b Part 1 checks Begin--------------------------------------------------#

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7b_1, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session7b_1, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7b_1)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_repr():
    '''
    Test the Repr function for the Class
    '''
    penta = session7b_1.Polygon(5, 8)
    assert len(str(penta)) > 10


def test_equality():
    '''
    Test whether two Polygons are Equal
    '''
    penta = session7b_1.Polygon(5, 8)
    penta_2 = session7b_1.Polygon(5, 8)
    assert penta == penta_2


def test_inequality():
    '''
    Test whether two Polygons are NOT Equal
    '''
    penta = session7b_1.Polygon(5, 8)
    penta_2 = session7b_1.Polygon(5, 10)
    assert penta != penta_2


def test_greater():
    '''
    Test One Polygon greather than other
    '''
    penta = session7b_1.Polygon(5, 8)
    octa = session7b_1.Polygon(8, 10)
    assert penta < octa

# ----------------------------------------------7b Part 1 checks End --------------------------------------------------#


# ----------------------------------------------7b Part 2 checks Begin--------------------------------------------------#

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7b_2, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session7b_2, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7b_2)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_repr():
    '''
    Test the Repr function for the Class
    '''
    penta = session7b_2.PolySeq(5, 8)
    assert len(str(penta)) > 10


def test_max_eff():
    '''
    Test the max_effeciency property of Sequence
    '''
    pol25 = session7b_2.PolySeq(25, 10)
    assert 25 in pol25.max_eff

# ----------------------------------------------7b Part 2 checks End --------------------------------------------------#
