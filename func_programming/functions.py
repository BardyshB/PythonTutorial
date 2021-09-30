def foo(a, b, c=None, d=None, e=1):
    return a, b, c, d, e


def foo_1(*args, c=None, d=None, e=1):
    a, b = args
    return a, b, c, d, e


def foo_2(*args, c=None, d=None, e=1):
    args = list(args)
    args.extend([c, d, e])
    return args


def foo_3(*args, **kwargs):
    return args, kwargs


def foo_4(*args, **kwargs):
    pass


a = 5


def foo_5(*args, **kwargs):
    global a
    a = 1


foo_6 = lambda *args, **kwargs: args[1]

# Lambda usage example:

x = [('a', 'F'), ('b', 'd'), ('c', 'E')]

x = list(map(
    lambda args: (args[0].upper(), args[1]),
    [
        ('a', 'F'),
        ('b', 'd'),
        ('c', 'E')
    ]
))
