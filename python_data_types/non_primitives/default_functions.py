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
"""
SET default functions
"""
# add
a = {1, 2, 'f'}
print('a=', a)
a.add('b')
print("a.add('b')=", a)
# clear
a = {1, 2, 'f'}
print('a=', a)
a.clear()
print("a.clear() = ", a)
# copy
c = {1, 2, 3}
d = c.copy()
print(d)
print('c is d', c is d)
# difference
c = {1, 2, 3, 5}
d = {'1', '2', '3', 5}
print('c.difference(d)=', c.difference(d))
print('d.difference(c)=', d.difference(c))
# difference_update
c = {1, 2, 3, 5}
d = {1, '2', '3', 5}
c.difference_update(d)
print('c.difference_update(d)=', c)
c = {1, 2, 3, 5}
d = {1, '2', '3', 5}
d.difference_update(c)
print('d.difference_update(c)=', d)
# discard
c = {1, 2, 3, 5}
print('c=', c)
c.discard(1)
print('c.discard(1)=', c)
# intersection
c = {1, 2, 3, 5}
d = {1, '2', '3', 5}
print('d.intersection(c)=', d.intersection(c))
# intersection_update
c = {1, 2, 3, 5}
d = {1, '2', '3', 5}
c.intersection_update(d)
print('c.intersection_update(d)=', c)
# isdisjoint
c = {1, 2, 3, 5}
d = {1, '2', '3', 5}
print('c.isdisjoint(d)=', c.isdisjoint(d))
c = {1, 2, 3, 5}
d = {'1', '2', '3', '5'}
print('c.isdisjoint(d)=', c.isdisjoint(d))
# issubset
c = {1, 5}
d = {1, '2', '3', 5}
print('c.issubset(d)=', c.issubset(d))
# issuperset
c = {1, 2, 3, 5}
d = {1, 2, 3, '2', '3', 5}
print('c.issuperset(d)=', d.issuperset(c))
# pop
d = {1, 2, 3, '2', '3', 5}
print('d.pop()=', d.pop())
print('d=', d)
# remove
d = {1, 2, 3, '2', '3', 5}
d.remove(2)
print('d.remove(2)=', d)
# symmetric_difference
c = {1, 2, 3, 5}
d = {1, 2, 3, '2', '3', 5}
print('c.symmetric_difference(d)=', d.symmetric_difference(c))
# symmetric_difference_update
c = {1, 2, 3, 5}
d = {1, 2, 3, '2', '3', 5}
d.symmetric_difference_update(c)
print('d.symmetric_difference_update(c)=', d)
# union
c = {1, 2, 3, 5}
d = {1, 2, 3, '2', '3', 5}
print('c.union(d)=', c.union(d))
# update
c = {1, 2, 3, 5}
d = {1, 2, 3, '2', '3', 5}
c.update(d)
print('c.update(d)=', c)
"""
FROZENSET default functions
"""
# copy
c = frozenset({1, 2, 3})
d = c.copy()
print(d)
print('c is d', c is d)
# difference
c = frozenset({1, 2, 3, 5})
d = frozenset({'1', '2', '3', 5})
print('c.difference(d)=', c.difference(d))
print('d.difference(c)=', d.difference(c))
# intersection
c = frozenset({1, 2, 3, 5})
d = frozenset({1, '2', '3', 5})
print('d.intersection(c)=', d.intersection(c))
# isdisjoint
c = frozenset({1, 2, 3, 5})
d = frozenset({1, '2', '3', 5})
print('c.isdisjoint(d)=', c.isdisjoint(d))
c = frozenset({1, 2, 3, 5})
d = frozenset({'1', '2', '3', '5'})
print('c.isdisjoint(d)=', c.isdisjoint(d))
# issubset
c = frozenset({1, 5})
d = frozenset({1, '2', '3', 5})
print('c.issubset(d)=', c.issubset(d))
# issuperset
c = frozenset({1, 2, 3, 5})
d = frozenset({1, 2, 3, '2', '3', 5})
print('c.issuperset(d)=', d.issuperset(c))
# symmetric_difference
c = frozenset({1, 2, 3, 5})
d = frozenset({1, 2, 3, '2', '3', 5})
print('c.symmetric_difference(d)=', d.symmetric_difference(c))
# union
c = frozenset({1, 2, 3, 5})
d = frozenset({1, 2, 3, '2', '3', 5})
print('c.union(d)=', c.union(d))
