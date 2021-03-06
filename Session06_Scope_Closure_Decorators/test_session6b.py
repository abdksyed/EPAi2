import pytest
import session6b
import os
import inspect
import re
import test_session6b
from datetime import datetime

README_CONTENT_CHECK_FOR = [
    'log',
    'run_odd',
    'authenticate',
    'time',
    'access',
    'decorator',
    'closure',
    'factory'
]


CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile(
        "Session06_Scope_Closure_Decorators/README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("Session06_Scope_Closure_Decorators/README.md",
                  "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("Session06_Scope_Closure_Decorators/README.md",
             "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You haven't well described your README.md file"


def test_readme_file_for_formatting():
    f = open("Session06_Scope_Closure_Decorators/README.md",
             "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6b, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session6b, inspect.isfunction)
    assert len(functions) > 15, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session6b, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session6b, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    functions = inspect.getmembers(session6b, inspect.isfunction)
    for function in functions:
        if function[0] != 'wraps':
            assert function[1].__annotations__


def test_rudodd_dec():
    '''
    Test whether the function runs at odd second or not using decorator
    '''
    @session6b.run_odd
    def test_func():
        return 'PASSED'
    if datetime.now().second % 2 != 0:
        assert test_func() == 'PASSED'
    else:
        assert test_func() != 'PASSED'


def test_runodd_dec_invalid_fn():
    '''
    Test whether the NOT a function throws an error when decorated using run_odd
    '''
    not_a_fn = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        session6b.run_odd(not_a_fn)


def test_log_dec(capfd):
    '''
    Test whether the function logs the correct data using decorator
    '''
    @session6b.log
    def test_func():
        return 'PASSED'
    res = test_func()
    out, err = capfd.readouterr()
    assert 'test_func' in out
    assert res == 'PASSED'


def test_log_dec_invalid_fn():
    '''
    Test whether the NOT a function throws an error when decorated using log
    '''
    not_a_fn = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        session6b.log(not_a_fn)


def test_auth_dec():
    '''
    Test whether the function is run by giving proper authentication using decorator
    '''
    @session6b.authenticate('admin', 'admin')
    def test_func():
        return 'PASSED'
    assert test_func() == 'PASSED'


def test_auth_dec_invalid_fn():
    '''
    Test whether the NOT a function throws an error when decorated using authenticate
    '''
    not_a_fn = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        session6b.authenticate('admin', 'admin')(not_a_fn)


def test_auth_dec_invalid_cred():
    '''
    Test whether the function is NOT run by giving IMproper authentication using decorator
    '''
    @session6b.authenticate('admin', 'adin')
    def test_func():
        return 'PASSED'
    with pytest.raises(ValueError):
        test_func()


def test_timed_dec(capfd):
    @session6b.timed(1000)
    def test_func():
        return 'PASSED'
    res = test_func()
    out, err = capfd.readouterr()
    assert 'test_func' in out
    assert float(out.split('\n')[1].split(' ')[7]) > float(
        out.split('\n')[1].split(' ')[18])/1000
    assert res == 'PASSED'


def test_timed_dec_invalid_fn():
    not_a_fn = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        session6b.timed(100)(not_a_fn)
