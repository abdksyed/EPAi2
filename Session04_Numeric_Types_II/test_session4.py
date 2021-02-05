import pytest
import random
import string
import session4
import os
import inspect
import re
import math
import test_session4

README_CONTENT_CHECK_FOR = [
    'time_it',
    'print',
    'temp_converter',
    'speed_converter',
    'polygon_area',
    'squared_power_list',
    'repetitions',
    'run',
    'time',
]


def test_readme_exists():
    assert os.path.isfile(
        "Session04_Numeric_Types_II/README.md"), "README.md missing!"


def test_readme_contents():
    readme_words = [word for line in open(
        "Session04_Numeric_Types_II/README.md", 'r', encoding="utf-8") for word in line.split()]
    assert len(
        readme_words) >= 500, "Make your README.md interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("Session04_Numeric_Types_II/README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md"


def test_readme_file_for_formatting():
    f = open("Session04_Numeric_Types_II/README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    print(functions)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session4, inspect.isfunction)
    assert len(functions) >= 25, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session4, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert function[1].__annotations__


def test_time_invalid_fn():
    def temp():
        pass
    with pytest.raises(ValueError):
        session4.time_it(temp)


def test_time_invalid_repetition_value():
    with pytest.raises(ValueError):
        session4.time_it(print, repetitions=0)


def test_time_invalid_repetition_type():
    with pytest.raises(TypeError):
        session4.time_it(print, repetitions=3.0)


def test_timeit_return_values():
    res_dict = session4.time_it(
        print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5)
    assert isinstance(res_dict['fn_result'], type(None))
    assert isinstance(res_dict['total_time'], float)
    assert isinstance(res_dict['average_time'], float)
    assert res_dict['total_time'] > res_dict['average_time']


def test_spl_invalid_argument():
    with pytest.raises(TypeError):
        session4.squared_power_list('2', start=0, end=1)
        session4.squared_power_list(1, start=1.0, end=1)
        session4.squared_power_list(1, start=0, end=1.0)


def test_spl_return_type():
    assert type(session4.squared_power_list(1, start=1, end=1)
                ) == list, "Hey, you aren't returning a list!"


def test_spl():
    assert session4.squared_power_list(2, start=0, end=5) == [
        1, 2, 4, 8, 16, 32], "Nope! This ain't what we need"


def test_polygon_area_invalid_arguments():
    with pytest.raises(TypeError):
        session4.polygon_area('123', sides=4)
        session4.polygon_area(12, sides=12.5)


def test_polygon_area_invalid_values():
    with pytest.raises(ValueError):
        session4.polygon_area(-2, sides=4)
        session4.polygon_area(4, sides=8)


def test_polygon_area_traingle():
    assert math.isclose(session4.polygon_area(
        15, sides=3), 97.4279, abs_tol=0.01)


def test_polygon_area_square():
    assert math.isclose(session4.polygon_area(
        15, sides=4), 225, abs_tol=0.01)


def test_polygon_area_pentagon():
    assert math.isclose(session4.polygon_area(
        15, sides=5), 387.107, abs_tol=0.01)


def test_polygon_area_hexagon():
    assert math.isclose(session4.polygon_area(
        15, sides=6), 584.567, abs_tol=0.01)


def test_temp_converter_invalid_args():
    with pytest.raises(TypeError):
        session4.temp_converter('123', temp_given_in='c')
        session4.temp_converter(98, temp_given_in=['f'])


def test_temp_converter_invalid_value():
    with pytest.raises(ValueError):
        session4.temp_converter(123, temp_given_in='k')


def test_temp_converter():
    assert math.isclose(session4.temp_converter(
        100, temp_given_in='f'), 37.7777777777, abs_tol=0.01)
    assert math.isclose(session4.temp_converter(
        37.7777777777, temp_given_in='c'), 100, abs_tol=0.01)


def test_speed_converter_kmph_to_mps():
    assert session4.speed_converter(
        200, dist='m', time='sec') == 55.55555555555556, 'speed_converter gives incorrect output.'


def test_speed_converter_kmph_to_yardpday():
    assert session4.speed_converter(
        10, dist='yrd', time='day') == 262466.4, 'speed_converter gives incorrect output.'


def test_speed_converter_kmph_to_ftpm():
    assert session4.speed_converter(
        5, dist='ft', time='min') == 273.4033333333333, 'speed_converter gives incorrect output.'


def test_time_it_squared_power_list():
    res = session4.time_it(session4.squared_power_list, 2,
                           start=1, end=10, repetitions=1000)
    assert (res['average_time'] > 0 and res['average_time'] < res['total_time']
            ), 'Improper implementation of squared_power_list function, takes longer than usual to run!'


def test_time_it_polygon_area():
    res = session4.time_it(
        session4.polygon_area, 20, sides=4, repetitions=1000)
    assert (res['average_time'] > 0 and res['average_time'] < res['total_time']
            ), 'Improper implementation of polygon_area function, takes longer than usual to run!'


def test_time_it_temp_converter():
    res = session4.time_it(session4.temp_converter, 20,
                           temp_given_in='f', repetitions=1000)
    assert (res['average_time'] > 0 and res['average_time'] < res['total_time']
            ), 'Improper implementation of temp_converter function, takes longer than usual to run!'


def test_time_it_speed_converter_time():
    res = session4.time_it(session4.speed_converter, 20,
                           dist='yrd', time='sec', repetitions=1000)
    assert (res['average_time'] > 0 and res['average_time'] < res['total_time']
            ), 'Improper implementation of speed_converter function, takes longer than usual to run!'
