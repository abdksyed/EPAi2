import time
import math
import sys


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
