"""
Python Extra Data Types
"""

from collections import *

"""
deque - Basically the list with ability to faster add elements to start or end  - O(1) complexity vs O(n) for list
Syntax: deque([el1,el2..])
"""
dq = deque[1211, 'a', 'sfas']
print(dq)

"""
defaultdict - Same as dict but without raising an error when no key is found 
Syntax: defaultdict(default_factory)
"""
# Defining the dict and passing lambda as default_factory argument
d = defaultdict(lambda: "WTF")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

"""
namedtuple - Tuple with named and name-callable values 
"""
Employee = namedtuple(
    'Employee',
    ['first_name', 'last_name', 'country', 'jobs', 'salary']
)
andrew = Employee('Andrew', 'Brown', 'US', ['Developer', 'Manager'], 987)
print(andrew)

"""
UserDict - wrapper around dict objects to make creating subclasses easier
"""
dc = {'a': 1,
      'b': 2,
      'c': 3}
userD = UserDict(dc)
print(userD.data)

"""
UserList - wrapper around list objects to make creating subclasses easier
"""
L = [1, 2, 3, 4]
userL = UserList(L)
print(userL.data)

"""
UserString - wrapper around string objects to make creating subclasses easier
"""
d = 12344
userS = UserString(d)
print(userS.data)

"""
Counter - keeps track of how many times equivalent values are added.
"""
a = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(a)
b = Counter({'a': 2, 'b': 3, 'c': 1})
print(b)
c = Counter(a=2, b=3, c=1)
print(c)
d = Counter('gasgafgsaga')
print(d)
"""
OrderedDict - just like regular dictionaries but have some extra capabilities relating to ordering operations
"""
d1 = {'a': 1, 'b': 2, 'c': 56}
d = OrderedDict(d1)
print(d)

"""
ChainMap - groups multiple dicts or other mappings together to create a single, updateable view
"""
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = ['eee']
d4 = (1, 5, 6, 47)
d5='aaaa'
c = ChainMap(d1, d2, d3,d4,d5)
print(reversed(c.maps))
