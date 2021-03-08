# Session 6a - Scopes and Closures

### [Hand Written Notes](https://github.com/abdksyed/EPAi2/blob/main/Session06_Scope_Closure_Decorators/notebooks/HandNotes.pdf)

### [Class Notebook - Closures](https://github.com/abdksyed/EPAi2/blob/main/Session06_Scope_Closure_Decorators/notebooks/Closures.ipynb)  
Click on **Open in Colab** for hands-on.

### Topic Covered:

* #### Global and Local Scope
* #### Non Local Scope
* #### Closures
* #### Closure Applications


# Assignment 6(a)

## Assignment Objective - Creation of Closures.

The main goal here is to implement nested functions and closures. Walking through the use cases, one will realize that closures are an effective way to implement certain functionalities that require some data abstraction and also be used in place of classes for some use cases. This also helps in reducing the memory overhead.

### Scan Fucntion (Docstring Length Check) 

The idea here is to check if a given function has proper docstring, whose character count should be at least 50. The value 50 is passed as a free variable and the functionality is implemented through closure.

```python
def scan_fn(scan_len: int) -> Callable:
    """
    Function to implement closure, encapsulates a function
    that checks whether an input function has a proper docstring,
    with length of atleast 50 characters.
    """
    def check_doc(fn: Callable) -> bool:
        """
        This is the inner function that actually checks the 
        docstring legth.
        Input: Function for which the docs has to be checked.
        Output: True if doc length > 50 else False
        """
        if not isinstance(fn, Callable):
            raise TypeError("Expected function!")
        return len(fn.__doc__) > scan_len
    return check_doc
```

### Next Fibonacci!!

Here, we have a function which is used to generate Fibonacci numbers, by making use of closure. The free variables hold the record of what was the last fetched fibonacci number and accordingly, whenever the respective function is called, it returns the next number in the sequence.

```python
def fib() -> Callable:
    """
    Function to implement closure, encapsulates a function
    that automatically gives you the next fibonacci number.
    Keeping track of the last fibonacci numbers is the task
    of free variables.
    """
    num_1, num_2 = 1, 1
    count = 0

    def next_fib() -> int:
        """
        Returns the next fibonacci number in the sequence.
        """
        nonlocal num_1, num_2, count
        count += 1
        if count <= 2:
            return num_2
        num_1, num_2 = num_2, num_1+num_2
        return num_2
    return next_fib
```

### Function call counter

Here, we have a global dictionary, which holds the number of times a particular function is called. There is no restriction to the function which might be called. If a function is called for the first time, it is added to the dictionary. The task was to implement this for add, mul, div functions, but this has been extended to accommodate any function that might be called.

Take a note that, apart from the global dictionary, we also have a dictionary as free variable to internally keep track of the count. This is to make correct updates of the function call counts, even if the user alters the global dictionary. As previous functions, we make use of closure to implement these functionalities.

```python
# Global dictionary that holds the number of times a particular function is called.
func_count = {}
def counter() -> Callable:
    """
    Function to implement closure, encapsulates a function
    that keeps tracks of how many times a particular function
    has been called. It updates a global list with count, and
    also mantains a free variable list so as to not let user 
    alter the count.
    """
    counter = {}

    def count(func: Callable, *args, **kwargs) -> Callable:
        """
        Updates and keeps track of the number of times, 
        a function might be called.
        Input: function and *args and *kwargs to be passed
                to the function
        Returns: Returned value from the function, called with
                provided parameters.
        """
        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        func_count[func.__name__] = counter[func.__name__]
        return func(*args, **kwargs)
    return count
```

### Function call counter - user differentiable

This call counter implementation is also similar to the previous one, except that this time the user is supposed to provide a dictionary explicitly and all the count updates would be made to it instead of that global dictionary in the previous case.

```python
def counter_users(user_dict: dict) -> Callable:
    """
    Function to implement closure, encapsulates a function
    that keeps tracks of how many times a particular function
    has been called. It updates a list, provided by user, with count,
    and also mantains a free variable list so as to not let user 
    alter the count.
    """
    counter = {}
    if not isinstance(user_dict, dict):
        raise TypeError('Expected Dictionary')

    def count(func: Callable, *args, **kwargs) -> Callable:
        """
        Updates and keeps track of the number of times, 
        a function might be called.
        Input: function and *args and *kwargs to be passed
                to the function
        Returns: Returned value from the function, called with
                provided parameters.
        """
        if not isinstance(func, Callable):
            raise TypeError("Expected function!")
        nonlocal counter
        counter[func.__name__] = counter.get(func.__name__, 0) + 1
        user_dict[func.__name__] = user_dict.get(
            func.__name__, 0) + 1
        return func(*args, **kwargs)
    return count
```

# Session 6b - Decorators

### [Class Notebook - Decorators](https://github.com/abdksyed/EPAi2/blob/main/Session06_Scope_Closure_Decorators/notebooks/Decorators_Part_1.ipynb)
### [Class Notebook - Decorators Part II](https://github.com/abdksyed/EPAi2/blob/main/Session06_Scope_Closure_Decorators/notebooks/Decorators_Part_2.ipynb)   
Click on **Open in Colab** for hands-on.

### Topic Covered:

* #### Decorators
* #### Parametrized Decorators
* #### Memoization
* #### Single Dispatch


# Assignment 6(b)

## Assignment Objective - Creation of Closures.

The main goal here is to implement Decorators and Decorator Factories. Walking through the use cases, one will realize that closures are an effective way to implement certain functionalities that require some data abstraction and also be used in place of classes for some use cases. This also helps in reducing the memory overhead. And this Closure can be used in a special way to acheive Decorators to decorate other functions.

### Run Odd (Run the Function when the Time is Odd Seconds) 

```python
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

@run_odd
def test(a, b):
    return a+b
```
### Log (Logs the info about Function whenever it's called)

```python
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

@log
def test(a, b):
    return a+b

```

### Authenticate (Decorator Factor - Which generates a Decorator and which indeed check for correct authentication and run if matched with database)

```python
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

@authenticate('admin', 'admin')
def add(a, b):
    return a+b
```

### Timed (Times the Total and Average time for the Function to Run for number of times provided by user)

```python
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


@timed(10000000)
def add(a, b):
    return a+b

```

### Access - (Decorator Factory using Class)

```python
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

@access(3, 'almost_there')
def budget_total(details):
    return f'{sum([int(x[:3]) for x in details[2]])}M'
```