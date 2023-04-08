# ----------- 2022-02-05------------------------
# TODO: use demo.py to review knowledge in day 27 GUI with tkinter and adcanved argument

def show(**kwargs):
    var_1 = kwargs.get("a")
    var_2 = kwargs.get("b")
    var_3 = kwargs.get("c")
    print(var_1)
    print(var_2)
    print(var_3)


def add(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)

def multiple(n1,n2=2):
    """ multiple n1 ,return it multiple by 2"""
    double = n1 * n2
    print(double)
# **kwargs
show(b=1)

# * args

add(1, 2, 3, 4, 5)
multiple(4,n2=30)
