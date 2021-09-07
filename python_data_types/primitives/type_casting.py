"""
Primitive Data Type Casting
"""

"""
Convert float to int and vice versa
"""

input_val = 1.0
print(input_val)

input_val = int(input_val)
print(input_val)

input_val = float(input_val)
print(input_val)

"""
Convert int to complex and vice versa

# Note! You can't cast from complex to int or to float
"""

input_val = 1
print(input_val)

input_val = complex(input_val)
print(input_val)

"""
Convert integer or float or string to boolean

Everything that is not 0 or 0.0 or '' is True
"""

print(
    bool(0)
)

print(
    bool(1)
)

print(
    bool(2)
)

print(
    bool(0.0)
)

print(
    bool(2.0)
)

print(
    bool('')
)

print(
    bool('foo')
)

"""
Convert string to integer or float
"""
print(
    int('1')
)
print(
    float('1')
)

# this will rise error
# print(
#     int('1.0')
# )

print(
    float('0.1')
)

print(
    float('00.11')
)

"""
Every primitive data type in python can be converted to string object
"""
print(
    str(1)
)
print(
    str(.1)
)
print(
    str(complex(1))
)
print(
    str(1 + 2j)
)
print(
    str(True)
)
print(
    str(False)
)
