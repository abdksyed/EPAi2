# Session 4 - Numeric Types II

### [Class Notebook]()
Click on **Open in Colab** for hands-on.

### Topic Covered:
* #### Booleans
* #### Booleans Precedence and Short Circuiting
* #### Arguments & Parameters: Positional & Keyword Argument
* #### Unpacking
* #### Extended Unpacking
* #### \*args
* #### Keyword Arguments
* #### \*\*kwargs
* #### All Together

# Assignment 4

## Assignment Objective - Computing Average Run Time of various functions.

### Classes and Functions used:

We have some functions that make use of positional and keyword arguments as described below. We also make use of `*args `and `*kwargs`.

## time_it

It takes a function, the positional and keyword arguments for that function, and gives an average figure of time taken per call to that function over a number of repetitions, which is also specified by the user.

```python
def time_it(fn: 'function', *args, repetitions: int = 1, **kwargs) -> tuple:
    '''
    Function to give average run time per call.
    Arguments:
        fn : Function to be run.
        *args: Arguments
        repetitions: Number of times fn must be called. Key word Argument. Default value: 1
        **kwargs: Keyword Arguments
    Return:
        Average Run Time.
    '''
    if fn not in [print, squared_power_list, polygon_area, temp_converter, speed_converter]:
        raise ValueError('Invalid Value Given for fn.')
    if repetitions <= 0:
        raise ValueError('repetiion value must be greater than Zero')
    if not isinstance(repetitions, int):
        raise TypeError('repetitions must be of type <int>')

    start = time.perf_counter()
    returned = None
    for _ in range(repetitions):
        returned = fn(*args, **kwargs)
    end = time.perf_counter()
    print(
        f'Total Time and Average Time to run the function {fn.__name__} are {end-start:.4f} seconds and {(end-start)/repetitions:.7f} seconds and it returned {returned}')
    return {'total_time': end-start, 'average_time': (end-start)/repetitions, 'fn_result': returned}
```


## squared_power_list

This function takes a number, as positional argument and two keyword arguments namely, start and end. It returns a list holding the power of that number from start to end. So if we give 2 as the number and start and end as 0 and 3 respectively, it will return [1, 2, 4, 8].

```python
def squared_power_list(number: int = 1, *, start: int = 0, end: int = 1) -> list:
    '''
    Calculates powers of a number, from start to end
    Arguments:
        number: a number whose powers are to be calculated
        start: which power to start from. Default:0
        end: which power to end with. Default:1
    Return:
        List of powers of a number from start to end.
    '''
    if not isinstance(number, (int, float)):
        raise TypeError('number should be of type <int> or <float>')
    if not isinstance(start, int):
        raise TypeError('start should be of type <int>')
    if not isinstance(end, int):
        raise TypeError('end should be of type <int>')

    pow_list = []
    for i in range(start, end+1):
        pow_list.append(number**i)
    return pow_list

```

## polygon_area

This function calculates area for a regular polygon with `sides` ranging from 3 to 6. It takes the length of the side  to calculate the area of the polygon and returns the area in float.

```python
def polygon_area(side_length: int = 1, *, sides: int = 3) -> float:
    '''
    Calculates Area of Polygon (3-sided to 6-sided)
    Arguments:
        side_length: Length of the polygon side, Default:1
        sides: Number of sides. Default:3
    Return:
        Area of the Polygon.
    '''
    if not isinstance(side_length, (int, float)):
        raise TypeError('side_length should be of type <int> or <float>')
    if not isinstance(sides, int):
        raise TypeError('sides should be of type <int>')

    if side_length <= 0:
        raise ValueError('Length of the Polygon must be greater than Zero.')
    if sides not in (3, 4, 5, 6):
        raise ValueError('Side of the Polygon must be 3,4,5 or 6')

    area = {3: (math.sqrt(3)/4)*(side_length**2), 4: side_length**2,
            5: 1/4*(math.sqrt(5*(5+2*math.sqrt(5))))*(side_length**2),
            6: (3*math.sqrt(3)/2)*(side_length**2)}
    return area.get(sides, 'ERROR')
```

##  temp_converter

The function takes in temperature as a positional argument and the unit of given argument as a keyword argument and converts it into the other unit of temperature. If the given temperature is in Celsius, the returned is in Fahrenheit an vice versa. Internally, two lambda functions take care of the calculations.

```python
def temp_converter(input_temp: float = 0, *, temp_given_in: str = 'f') -> float:
    '''
    Covertes Fahrenheit to Celsius or Celsius to Fahrenheit.
    Arguments:
        input_temp: The input temp which is to be converted. Default:0
        temp_given_in: The Given Temperature class (Fahrenheit or Celsius). Default: 'f'
    Returns:
        Converted Temp float.
    '''
    if not isinstance(input_temp, (int, float)):
        raise TypeError('input_temp should be of type <int> or <float>')
    if not isinstance(temp_given_in, str):
        raise TypeError('temp_given_in should be of type <str>')

    if temp_given_in in ['f', 'F', 'Fahrenheit', 'fahrenheit']:
        return (input_temp - 32)*(5/9)
    elif temp_given_in in ['c', 'C', 'Celsius', 'celsius']:
        return (input_temp * (9/5)) + 32
    else:
        raise ValueError(
            "Invalid Temperature type. Please provide either 'f' or 'c'")
```


## speed_converter

This function converts the given speed (given in kmph by default) to preferred units of distance and time. It takes input speed in `kmph` and converts into the specified units of speed according to dist and time parameters. `dist` parameter can take values (km/m/ft/yard) and `time` parameter can take values unit (ms/sec/min/hr/day).

```python
def speed_converter(speed: float, *, dist: str = 'km', time: str = 'min') -> float:
    '''
    A Speed Converter. Distances - km/m/ft/yrd. Time -  ms/s/m/hr/day.
    Arguments:
        speed: The input given speed value in kmph.
        dist: The unit of distance to be converted in.
        time: The unit of time to be converted in.
    Returns:
        Converted speed float from kmph to dist/time unit.
    '''
    dist_dict = {'km': 1, 'm': 1000, 'ft': 3280.84, 'yrd': 1093.61}
    time_dict = {'hr': 1, 'day': 1/24, 'min': 60, 'sec': 3600, 'ms': 3600000}

    if not dist_dict.get(dist, 0):
        raise ValueError(
            'Incorrect Distance Selected. dist input must be either of km/m/ft/yrd')
    if not time_dict.get(time, 0):
        raise ValueError(
            'Incorrect Time Selected. time input must be either of ms/s/m/hr/day')

    return speed * (dist_dict[dist]/time_dict[time])
```

### Test Cases Run:

```test_function_annotations``` -> Test for Annotations in Each Function  
```test_function_count``` -> Test for the number of Test cases present (>= 25)  
```test_function_doc_string``` -> Test for Docstrings present for each Fucntions.  
```test_function_name_had_cap_letter``` -> Test for PEP guidlines for Function name(no capital letters)  
```test_function_repeatations``` -> Test for repeatition of test functions.  
```test_indentations``` -> Test for indentations in the code (must be 4 spaces throughout)  
```test_polygon_area_hexagon``` -> Test for polygon_area. Area of Hexagon  
```test_polygon_area_invalid_arguments``` -> Test for polygon_area. Invalid Type of Arguments  
```test_polygon_area_invalid_values``` -> Test for polygon_area. Invalid Value of Arguments  
```test_polygon_area_pentagon``` -> Test for polygon_area. Area of Pentagon  
```test_polygon_area_square``` -> Test for polygon_area. Area of Square  
```test_polygon_area_traingle``` -> Test for polygon_area. Area of Triangle  
```test_readme_contents``` -> Test for checking README.md file length  
```test_readme_exists``` -> Test for checking README.md file existence  
```test_readme_file_for_formatting``` -> Test for checking the formatting of README.md  
```test_readme_proper_description``` -> Test for checking README.md file contents description  
```test_speed_converter_kmph_to_ftpm``` -> Test for Checking speed_sonverter. km/h to feet/m  
```test_speed_converter_kmph_to_mps``` -> Test for Checking speed_sonverter. km/h to miles/sec    
```test_speed_converter_kmph_to_yardpday``` -> Test for Checking speed_sonverter. km/h to yard/day  
```test_spl``` -> Test for checking squared_power_list. List of Powers of 2  
```test_spl_invalid_argument``` -> Test for squared_power_list. Invalid Type of Arguments    
```test_spl_return_type``` -> Test for squared_power_list. Checking Invalid Return Type  
```test_temp_converter``` -> Test temp_converted. Converting 'f' to 'c' and vice versa  
```test_temp_converter_invalid_args``` -> Test for temp_converted. Invalid Type of Arguments  
```test_temp_converter_invalid_value``` -> Test for temp_converter. Invalid Value of Arguments  
```test_time_invalid_fn``` -> Test for time_it Function. Passing invalid function argument  
```test_time_invalid_repetition_type``` -> Test for time_it Function. Passing invalid repitition type.  
```test_time_invalid_repetition_value``` -> Test for time_it Function. Passing invalid repitition value.  
```test_time_it_polygon_area``` -> Test for time_it Function. Testing polygon_area time.  
```test_time_it_speed_converter_time``` -> Test for time_it Function. Testing speed_converter time.  
```test_time_it_squared_power_list``` -> Test for time_it Function. Testing squared_power_list time.  
```test_time_it_temp_converter``` -> Test for time_it Function. Testing temp_converter time.  
```test_timeit_return_values``` -> Test for time_it Function. Testing return_value.  