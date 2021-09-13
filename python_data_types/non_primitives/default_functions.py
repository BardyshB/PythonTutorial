"""
Each data type has default function
"""

"""
LIST default functions
"""

# append
a = []
print(a)
a.append(1)
print(a)
# clear
b = [1, 2, 3]
print(b)
b.clear()
print(b)
# copy
c = [1, 2, 3]
d = c.copy()
print(d)
print('c is d', c is d)
# count
e = [1, 2, 3, 4, 1, 1, 2]
print('e.count(1)', e.count(1))
print('e.count(2)', e.count(2))
# extend
f = [1, 2, 3, 4]
g = [1, 1, 2]
print('f=', f)
print('g=', g)
f.extend(g)
print('f=', f)
# index
h = [1, 2, 3, 4]
print('h.index(3)', h.index(3))
# insert
k = [1, 2, 3, 4]
print('k=', k)
k.insert(0, 5)
print('k.insert(0, 5)', k)
# pop
l = [1, 2, 3, 4]
print('l=', l)
l.pop()
print('l.pop()', l)
# remove
m = ['foo', 'bar', 'lol', 'lorem']
print('m=', m)
m.remove('bar')
print('m.remove("bar")', m)
# reverse
n = [1, 2, 3, 4]
print('n=', n)
n.reverse()
print('n.reverse()', n)
# sort
o = [4, 1, 2, 6]
print('n=', o)
o.sort()
print('o.sort()', o)

"""
TUPLE default functions
"""

# count
e = (1, 2, 3, 4, 1, 1, 2)
print('e.count(1)', e.count(1))
print('e.count(2)', e.count(2))
# index
h = (1, 2, 3, 4)
print('h.index(3)', h.index(3))

"""
DICT default functions
"""
# clear
k = {1: 2, 'foo': 'bar'}
print('k=', k)
k.clear()
print('k=', k)
# copy
k = {1: 2, 'foo': 'bar'}
d = c.copy()
print(d)
print('c is d', c is d)
# fromkeys
k = {1: 2, 'foo': 'bar'}
print(k.fromkeys(k.keys()))
# get
k = {1: 2, 'foo': 'bar'}
print('k.get(1)', k.get(1))
print('k.get("fo")', k.get('fo'))
# items
k = {1: 2, 'foo': 'bar'}
print('k.items() = ', k.items())
# keys
k = {1: 2, 'foo': 'bar'}
print('k.keys() = ', k.keys())
# pop
k = {1: 2, 'foo': 'bar'}
print('k.pop("foo") = ', k.pop("foo"))
# popitem
k = {1: 2, 'foo': 'bar'}
print('k.popitem() = ', k.popitem())
# setdefault
k = {1: 2, 'foo': 'bar'}
print('k=', k)
k.setdefault('lol')
print('k.setdefault() = ', k)
# update
k = {1: 2, 'foo': 'bar'}
print('k=', k)
k.update({1: 4})
print('k.update({1: 4}) = ', k)
# values
k = {1: 2, 'foo': 'bar'}
print('k.values() = ', k.values())
