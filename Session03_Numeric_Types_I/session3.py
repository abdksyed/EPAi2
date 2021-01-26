from fractions import Fraction


def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if (base < 2) or (base > 36):
        raise ValueError('The base value must be between 2 and 36')

    if len(digit_map) != base:
        raise ValueError(
            f'Got {len(digit_map)} characters in digit_map instead of {base}')
    if len(digit_map) != len(set(digit_map)):
        raise ValueError("digit_map can't have repeating characters.")

    if number < 0:
        sign = '-'
        number *= -1
    else:
        sign = ''

    n = number
    enc = []
    while n > 0:
        n, m = divmod(n, base)
        enc.insert(0, digit_map[m])
    return sign + ''.join(enc)


def float_equality_testing(a, b):
    '''
    This function emulates the ISCLOSE method from the MATH module, but you can't use this function
    We are going to assume:
    - rel_tol = 1e-12
    - abs_tol = 1e-05
    Arguments:
    a -> float, First Number
    b -> float, Second Number which is check for equality with a
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05

    if a == b:  # short ciruiting
        return True
    return abs(a-b) <= max(rel_tol * (max(abs(a), abs(b))), abs_tol)


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.trunc method. It ignores everything after the decimal point.
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    Arguments:
    f_num -> float, A floating number which is to be truncated
    Returns:
    Truncated number.
    '''
    return f_num // 1 if f_num >= 0 else f_num//1 + 1


def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function.
    You are not allowed to use ROUND function, but expected to write your one manually.
    Arguments:
    f_num -> float, A floating number which is to be rounded off
    Returns:
    Rounded Number wihtout decimals.
    '''
    return Fraction(f_num).limit_denominator(1)


def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    if f_num - f_num//1 >= 0.5:
        return f_num//1 + 1
    else:
        return f_num//1
