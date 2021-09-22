"""
Python Extra Data Types
"""
from collections import *
import timeit

"""
deque
"""
# append speed test
timeit.timeit('list_object.append("a")', setup='list_object=[]', number=1000000)
timeit.timeit('deque_object.append("a")', setup='import collections as cl; deque_object=cl.deque()', number=1000000)

# append left speed test
timeit.timeit('list_object.insert(0, "a")', setup='list_object=[]', number=10000)
timeit.timeit('deque_object.appendleft("a")', setup='import collections as cl; deque_object=cl.deque()', number=10000)

# pop speed test
timeit.timeit('list_object.pop()', setup='list_object=list(range(1000000))', number=1000000)
timeit.timeit('deque_object.pop()', setup='import collections as cl; deque_object=cl.deque(range(1000000))', number=1000000)

# popleft speed test
timeit.timeit('list_object.pop(0)', setup='list_object=list(range(1000000))', number=10000)
timeit.timeit('deque_object.popleft()', setup='import collections as cl; deque_object=cl.deque(range(1000000))', number=10000)


"""
defaultdict
"""

"""
namedtuple
"""

"""
UserDict
"""

"""
UserList
"""

"""
UserString
"""

"""
Counter
"""
c = Counter()
"""
OrderedDict
"""

"""
ChainMap
"""
ch = ChainMap()
