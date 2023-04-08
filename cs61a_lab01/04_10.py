# Disc 01 : Control, environment diagrams
##TODO: Q2: Jacket Weather?
def wears_jacket_with_if(temp,is_rain):
    """
        >>> wears_jacket_with_if(90, False)
        False
        >>> wears_jacket_with_if(40, False)
        True
        >>> wears_jacket_with_if(100, True)
        True
        """

    return True if temp < 60 or is_rain else False

## TODO: Q3: If Function vs Statement
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()
def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    "*** YOUR CODE HERE ***"
    # expression
    return 3==2
def true_func():
    "*** YOUR CODE HERE ***"
    return print("Welcome to")

def false_func():
    "*** YOUR CODE HERE ***"
    return print("61A")


## TODO:    q5
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    dividion = 2
    while dividion < n:
        if n % dividion == 0:
            return False
        dividion += 1
    return True

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if i % 5 == 0 and i % 3 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
        i += 1

