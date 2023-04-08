def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(1,2,3))
