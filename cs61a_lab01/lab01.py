def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    elif k > 0:
        result = n
        while k > 1:
            n = n - 1
            result *= n
            k -= 1
        return result
def falling2(n,k):
    """
    return falling with recursive computation

    >>> falling(6, 3)  # 6 * 5 * 4
    120

    :param n:
    :param k:
    :return:
    """
    if k == 0:
        return 1
    else:
        return n * falling2(n-1,k-1)


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    digits = [int(num) for num in str(y)]
    sum = 0
    for digit in digits:
        sum += digit
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if '88' in str(n):
        return True
    else:
        return False


print(double_eights(12345))
print(falling(6, 3))
print(sum_digits(10))
