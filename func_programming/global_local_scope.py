a = 2


def foo_local():
    a = 1
    return a


def foo_global():
    global a
    a = 1
    return a


foo_global()
