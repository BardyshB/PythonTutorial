"""
Python Non Primitive Data Types
"""

"""
LIST EXAMPLE
"""
a = [1, 2, 3, 4]
b = ['1', '2', 'foo', 'bar']
c = [1, '1', '2', 'foo', 123]

"""
TUPLE EXAMPLE
"""
d = (1, 2, 3, 4)
e = ('1', '2', 'foo', 'bar')
f = (1, '1', '2', 'foo', 123)

"""
DICTIONARY EXAMPLE
"""
g = {
    'foo': 'bar',
    '1': '2',
    1: '2',
    2: 2,
    (1, 23): 'lol',
    1.2: 'lorem'
}
h = dict(
    foo='bar',
    lorem='ipusum'
)

"""
SET EXAMPLE
"""
i = {'foo', 'bar', '1', '2', 1, '2', 2, 2, (1, 23), 'lol', 1.2, 'lorem'}
j = set((1, 2, 3, 4, 5, 6, 'da'))


"""
FROZEN SET EXAMPLE
"""
k = frozenset({'foo', 'bar', '1', '2', 1, '2', 2, 2, (1, 23), 'lol', 1.2, 'lorem'})
l = frozenset((1, 2, 3, 4, 5, 6, 'da'))
