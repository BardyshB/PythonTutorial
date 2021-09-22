"""
deque
"""

import collections

# Create a deque
DoubleEnded = deque(["Mon", "Tue", "Wed"])
print(DoubleEnded)
print(DoubleEnded[2])

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Thu")
print(DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print(DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print(DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print(DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print(DoubleEnded)

"""
defaultdict
"""
# Same functionality as for dict + default values


"""
namedtuple - Tuple with named and name-callable values 
"""
# Ordering of namedtuple elements doesn't matter when it's labled
Employee = namedtuple(
    'Employee',
    ['first_name', 'last_name', 'country', 'jobs', 'salary']
)
andrew = Employee('Andrew', 'Brown', 'US', ['Developer', 'Manager'], 9245)
anna = Employee(
    last_name='Stevenson',
    first_name='Anna',
    jobs=['Product Owner'],
    country='UK',
    salary=0
)
print(anna)
print(andrew)

# Access by index
print((andrew[0], andrew[2]))

# Access by named attributes
print((andrew.first_name, andrew.country))

# Show values as OrdererDict
emp = andrew._asdict()
print(emp)

# Unpacking named attributes using tuple assignment
first_name, last_name, country, jobs, salary = andrew
print(first_name, last_name, country, jobs, salary, sep='\n')

# Named Tuples are itterable
for attr in anna:
    print(attr)

"""
UserDict
"""


class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

print("Original Dictionary")
print(d)

d.pop(1)

"""
UserList
"""
# Creating a userlist
userL = UserList(L)
print(userL.data)

# Creating empty userlist
userL = UserList()
print(userL.data)


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deletion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from
    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")


# Driver's code
L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
L.remove()

"""
UserString
"""


# Creating a Mutable String
class Mystring(UserString):

    # Function to append to
    # string
    def app(self, s):
        self.data += s

    # Function to remove from
    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")


# Driver's code
s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.app("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)

"""
Counter
"""
# Adding values to empty counter
c = Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': -100})
print('Dict    :', c)

# Clearing counter value
d = Counter('gsaggagas')
print(d)
d.clear()
print(d)

# Accessing count values
c = Counter('abcdaab')

for letter in 'abcde':
    print(letter, ':', c[letter])

# Create a list based of counter values
c = Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))

# Most common N values
c = Counter('What Fresh Hell Is This')
print('Most common:')
for letter, count in c.most_common(3):
    print(letter, 'is repeated ', count, 'times')

    # Most common N values - ordering
    c = Counter('cccWhat Fresh Hell Is This')
    print('Most common:')
    for letter, count in c.most_common(3):
        print(letter, 'is repeated ', count, 'times')

# Arithemtic operations
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = Counter('alphabet')

print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

# Each time a new Counter is produced through an operation, any items with zero or negative counts are discarded.
print('\nSubtraction:')
print(c2 - c1)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)
"""
OrderedDict
"""
# Move to end
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(''.join(d.keys()))

# Move to start
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b', last=False)
print(''.join(d.keys()))
"""
ChainMap
"""
# initializing dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}

# initializing ChainMap
chain = ChainMap(dic1, dic2)

# printing chainMap using maps
print("All the ChainMap contents are : ")
print(chain.maps)

# printing keys using keys()
print("All keys of ChainMap are : ")
print(list(chain.keys()))

# printing values using values() - returns the value from the first dict
print("All values of ChainMap are : ")
print(list(chain.values()))

# using new_child() to add new dictionary
dic3 = {'f': 5}
chain1 = chain.new_child(dic3)
print(chain1.maps)

# displaying value associated with b before reversing
print("Value associated with b before reversing is : ", end="")
print(chain1['b'])

# displaying value associated with b after reversing
chain1.maps = reversed(chain1.maps)
print("Value associated with b after reversing is : ", end="")
print(chain1['b'])
