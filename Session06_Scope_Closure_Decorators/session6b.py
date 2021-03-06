from datetime import datetime
from functools import wraps
from time import perf_counter


def run_odd(fn: callable) -> callable:
    '''
    function acts as a decorator which only allows the passed function to run
    only in odd seconds using closure.
    returns the closure
    '''
    if not callable(fn):
        raise TypeError("Not a Function!")

    @wraps(fn)
    def inner(*args, **kwargs):
        '''
        this inner function with the "fn" free variable
        becomes a closure.
        return fn result/fail string based on the current time second
        '''
        if datetime.now().second % 2 != 0:
            return fn(*args, **kwargs)
        else:
            return 'Not the Right Time.'
    return inner


def log(fn: callable) -> callable:
    '''
    function acts as a decorator which gives out calling logs for the passed
    function using closure.
    returns the closure
    '''
    if not callable(fn):
        raise TypeError("Not a Function!")

    @wraps(fn)
    def inner(*args, **kwargs):
        '''
        this inner function with the "func_name" free variable
        becomes a closure.
        return a call log with the result of the function.
        '''
        print(f'The function "{fn.__name__}" was called at {datetime.now()}.')
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print(
            f'The function "{fn.__name__}" took {end-start:.8f} seconds to run.')
        return result

    return inner


def authenticate(username: str, password: str) -> callable:
    '''
    The function acts as a decorator factory which takes the user password and
    return the authenticator decorator
    returns the decorator
    '''
    if not isinstance(password, str) or not isinstance(username, str):
        raise TypeError("Username/Password must be STRING")
    users = {'admin': 'admin', 'racheal': 'rossy_hubby', 'pete': 'iamCrusader'}

    def auth(fn: callable) -> callable:
        '''
        function acts as a decorator which checks the given password and then
        only allows the function to run using closure.
        returns the closure
        '''
        if not callable(fn):
            raise TypeError("Not a Function!")

        @wraps(fn)
        def inner(*args, **kwargs):
            '''
            this inner function with the "func_name"
            as free variable becomes a closure.
            return result of the function.
            '''
            if users[username] == password:
                print(f'{fn.__name__} access granted.')
                return fn(*args, **kwargs)
            else:
                raise ValueError('Access Denied!')
        return inner
    return auth


def timed(number_times: int) -> callable:
    '''
    The function acts as a decorator factory which takes
    the number of times the function is to be run and
    returns the decorator
    '''
    if not isinstance(number_times, int) and number_times <= 0:
        raise TypeError('The Number must be of type "int" and greater than 0.')

    def time_it(fn: callable) -> callable:
        '''
        function acts as a decorator which takes the function.
        and make the inner function run for n no. of times.
        returns the closure
        '''
        if not callable(fn):
            raise TypeError("Not a Function!")

        @wraps(fn)
        def inner(*args, **kwargs):
            print(
                f'The function "{fn.__name__}" is now running for {number_times} times.')
            start = perf_counter()
            for _ in range(number_times):
                result = fn(*args, **kwargs)
            end = perf_counter()
            print(
                f'The function "{fn.__name__}" took a total of {end-start:.8f} seconds to run.', end='')
            print(
                f' And an average time per run is {(end-start)/number_times:.8f} seconds.')
            return result
        return inner
    return time_it


class access():
    '''
    The class objects acts as a decorator factory which takes int access level as
    argument and give hierarchical access for the function parameter
    (ex. free vars).
    Valid Access level are [1,2,3,4]
    returns the decorator on calling object.
    '''
    _users = {1: 'low_baller', 2: 'Promoted',
              3: 'almost_there', 4: 'king_of_hill'}
    _team_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    _team_name = ['Mercedes', 'Ferrari', 'Red Bull', 'McLaren', 'Racing Point',
                  'Renault', 'Alpha Tauri', 'Alfa Romeo', 'Haas', 'Williams']
    _team_budget = ['660M', '800M', '630M', '400M',
                    '200M', '550M', '170M', '140M', '110M', '130M']
    _team_confidential = ['xxc13#', '554cx$', '334vf&',
                          '23f5b(', 'c6bj!', '66ty&', '9lop0%', 'cc4v5@', 'gg88b^', 'yx56c$']
    _data = (_team_no, _team_name, _team_budget, _team_confidential)

    def __init__(self, level: int, level_key: str) -> callable:
        if not isinstance(level, int) and level in [1, 2, 3, 4]:
            raise TypeError(
                'The level must be of type "int" and lie between 1 and 4.')
        if not isinstance(level_key, str):
            raise TypeError('The level key must be of type string')
        if self._users[level] != level_key:
            raise ValueError(
                'Sorry entered Level Key is invalid, "NO" Privilige Access Granted!')
        self.level = level

    def __call__(self, fn: callable):
        '''
        The object when called acts as a decorator which takes the function.
        and make the inner function give privildge accordingly.
        returns the closure
        '''
        if not callable(fn):
            raise TypeError("Not a Function!")

        @wraps(fn)
        def inner():
            try:
                return fn(self._data[:self.level])
            except IndexError:
                raise ValueError(
                    f'As per your Privilge access you can index the data only from 0 to {self.level-1}')

        return inner
