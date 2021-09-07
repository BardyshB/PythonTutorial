"""
Each data type has default function
"""

"""
INTEGER default functions
"""
# as_integer_ratio
# as integer is integer ratio will have always the same structure
# note: see the same function for float type
integer_value = 2
integer_value = integer_value.as_integer_ratio()
print(integer_value[0], "/", integer_value[1])

# bit_length

integer_value = 2
integer_value = integer_value.bit_length()
print(integer_value)  # result: 2 (00, 01, 10, 11)  | max binary - 11 | max denary - 3 | combination - 4

integer_value = 15
integer_value = integer_value.bit_length()
print(integer_value)  # result: 4                   | max binary - 1111 | max denary - 15 | combination - 16

# conjugate
integer_value = 15
integer_value = integer_value.conjugate()
print(integer_value)  # return complex conjugate of any int. Mainly used with complex type

# denominator
integer_value = 15
integer_value = integer_value.denominator
print(integer_value)

# from_bytes
# to_bytes

"""
INTEGER default properties
"""
# numerator and denominator
integer_value = 15
integer_value = integer_value.numerator
print(integer_value)
integer_value = 15
integer_value = integer_value.denominator
print(integer_value)

# imag
integer_value = 15
integer_value = integer_value.imag
print(integer_value)

# real
integer_value = 15
integer_value = integer_value.real
print(integer_value)

"""
FLOAT default functions
"""
# as_integer_ratio
float_value = 2.5
float_value = float_value.as_integer_ratio()
print(float_value[0], "/", float_value[1])

# conjugate
float_value = 2.5
float_value = float_value.conjugate()
print(float_value)  # return complex conjugate of any int. Mainly used with complex type

# is_integer
float_value = 2.5
float_value = float_value.is_integer()
print(float_value)
float_value = 2.0
float_value = float_value.is_integer()
print(float_value)

# fromhex
float_value = 2.0
float_value = float_value.fromhex('0x1.ffffp10')
print(float_value)  # return 2047.984375 as this number in hexadecimal 0x1.ffffp10

# hex
float_value = 2.0
float_value = float_value.hex()
print(float_value)  # return "0x1.4000000000000p+1" as hexadecimal string
# imag
float_value = 2.0
float_value = float_value.imag
print(float_value)

# real
float_value = 2.0
float_value = float_value.real
print(float_value)
"""
BOOLEAN default functions
"""
# as_integer_ratio
# bit_length
# conjugate
# denominator
# from_bytes
# imag
# numerator
# real
# to_bytes
"""
STRING default functions
"""
# capitalize
# casefold
# center
# count
# encode
# endswith
# expandtabs
# find
# format
# format_map
# index
# isalnum
# isalpha
# isascii
# isdecimal
# isdigit
# isidentifier
# islower
# isnumeric
# isprintable
# isspace
# istitle
# isupper
# join
# ljust
# lower
# lstrip
# maketrans
# partition
# replace
# rfind
# rindex
# rjust
# rpartition
# rsplit
# rstrip
# split
# splitlines
# startswith
# strip
# swapcase
# title
# translate
# upper
# zfill
