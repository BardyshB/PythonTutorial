"""
Each data type has default function
"""
import datetime

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

# from_bytes
integer_value = 1
integer_value = integer_value.to_bytes(integer_value, 'little')
print(integer_value)
# to_bytes
integer_value = 1
integer_value = integer_value.from_bytes(b'\x01', 'little')
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

"""
BOOLEAN default functions
"""
# as_integer_ratio
bool_value = True
bool_value = bool_value.as_integer_ratio()
print(bool_value)

# bit_length
bool_value = True
bool_value = bool_value.bit_length()
print(bool_value)

# conjugate
bool_value = True
bool_value = bool_value.conjugate()
print(bool_value)

# from_bytes
bool_value = True
bool_value = bool_value.to_bytes(bool_value, 'little')
print(bool_value)
# to_bytes
bool_value = True
bool_value = bool_value.from_bytes(b'\x01', 'little')
print(bool_value)

"""
STRING default functions
"""
# capitalize
str_val = 'test'
str_val = str_val.capitalize()
print(str_val)
# casefold
str_val = 'TEST'
str_val = str_val.casefold()
print(str_val)  # Return a version of the string suitable for caseless comparisons
# center
str_val = 'TEST'
str_val = str_val.center(100)
print(str_val)
# count
str_val = 'TEST'
str_val = str_val.count('T')
print(str_val)  # counts how many 'T' in string
# encode
str_val = 'TEST'
str_val = str_val.encode()
print(str_val)
# startswith
str_val = 'TEST'
str_val = str_val.startswith('T')
print(str_val)
str_val = 'TEST'
str_val = str_val.startswith('S')
print(str_val)
# endswith
str_val = 'TEST'
str_val = str_val.endswith('T')
print(str_val)
str_val = 'TEST'
str_val = str_val.endswith('S')
print(str_val)
# expandtabs
str_val = '             TEST'
print(str_val)
str_val = str_val.expandtabs()
print(str_val)  # replace \t with \s
# find
str_val = 'barbarian'
str_val = str_val.find('bar')
print(str_val)  # return index of string where searchable word starts
# rfind
str_val = 'barbarian'
str_val = str_val.rfind('bar')
print(str_val)
# format
str_val = 'SIMPLE STRING FORMATTING {}'
str_val = str_val.format('ipsum1')
print(str_val)
str_val = 'SIMPLE STRING FORMATTING {0}, {1}'
str_val = str_val.format('ipsum_test', 'ipsum_test')
print(str_val)
str_val = 'SIMPLE STRING FORMATTING {data}'
str_val = str_val.format(data='ipsum2')
print(str_val)
str_val = 'EXTRA STRING FORMATTING FLOAT NUMBER: {number:.4f}'
str_val = str_val.format(number=.123500000)
print(str_val)
str_val = 'EXTRA STRING FORMATTING FLOAT NUMBER AS PERCENTAGE: {number:%}'
str_val = str_val.format(number=.123500000)
print(str_val)
str_val = 'EXTRA STRING FORMATTING FLOAT NUMBER AS PERCENTAGE WITH TWO DECIMAL PLACES: {number:.2%}'
str_val = str_val.format(number=.123500000)
print(str_val)
str_val = 'EXTRA STRING FORMATTING FLOAT NUMBER AS SCIENCE NUMBER: {number:e}'
str_val = str_val.format(number=.123500000)
print(str_val)
str_val = 'EXTRA STRING FORMATTING FLOAT NUMBER: {number:.2e}'
str_val = str_val.format(number=.123500000)
print(str_val)
str_val = 'EXTRA STRING FORMATTING DATE: {date_value:%d, %b %Y}'
str_val = str_val.format(date_value=datetime.datetime.now())
print(str_val)
# format_map
str_val = "{x}'s last name is {y}'"
dict_with_data = {'x': 'John', 'y': 'Wick'}
str_val = str_val.format_map(dict_with_data)
print(str_val)
# index
str_val = "John's last name is Wick and his last trip was to .."
str_val = str_val.index('last')  # return index of letter that has first match
print(str_val)
# rindex
str_val = "John's last name is Wick and his last trip was to .."
str_val = str_val.rindex('last')  # return index of letter that has first match
print(str_val)
# isalnum
str_val = "John's last name is Wick"
str_val = str_val.isalnum()
print(str_val)
str_val = "1B2c"
str_val = str_val.isalnum()
print(str_val)
# isalpha
str_val = "1"
str_val = str_val.isalpha()
print(str_val)
str_val = "aZ"
str_val = str_val.isalpha()
print(str_val)
# isascii
str_val = "John's last name is Wick"
str_val = str_val.isascii()
print(str_val)
str_val = "Призвіще Джона є Вік"
str_val = str_val.isascii()
print(str_val)
# isdecimal
str_val = "1"
str_val = str_val.isdecimal()
print(str_val)
str_val = "1.0"
str_val = str_val.isdecimal()
print(str_val)
str_val = "1+2j"
str_val = str_val.isdecimal()
print(str_val)
# isdigit
str_val = "1"
str_val = str_val.isdigit()
print(str_val)
str_val = "11"
str_val = str_val.isdigit()
print(str_val)
str_val = "1.0"
str_val = str_val.isdigit()
print(str_val)
# isidentifier
str_val = "data"
str_val = str_val.isidentifier()
print(str_val)
str_val = "def"
str_val = str_val.isidentifier()
print(str_val)
str_val = "class"
str_val = str_val.isidentifier()
print(str_val)
str_val = "Jhon1"
str_val = str_val.isidentifier()
print(str_val)
str_val = "1Jhon"
str_val = str_val.isidentifier()
print(str_val)
# islower
str_val = "1Jhon"
str_val = str_val.islower()
print(str_val)
str_val = "1jhon"
str_val = str_val.islower()
print(str_val)
# isnumeric
str_val = "1Jhon"
str_val = str_val.isnumeric()
print(str_val)
str_val = "1325235"
str_val = str_val.isnumeric()
print(str_val)
# isprintable
str_val = ""
str_val = str_val.isprintable()
print(str_val)
str_val = "1"
str_val = str_val.isprintable()
print(str_val)
str_val = ''
str_val = str_val.isprintable()
print(str_val)
str_val = ''
str_val = str_val.isprintable()
print(str_val)
# isspace
str_val = ' '
str_val = str_val.isspace()
print(str_val)
str_val = '     '
str_val = str_val.isspace()
print(str_val)
str_val = '\t\t'
str_val = str_val.isspace()
print(str_val)
# istitle
str_val = 'Test'
str_val = str_val.istitle()
print(str_val)
str_val = 'test'
str_val = str_val.istitle()
print(str_val)
# isupper
str_val = 'Test'
str_val = str_val.isupper()
print(str_val)
str_val = 'TEST'
str_val = str_val.isupper()
print(str_val)
# join
str_val = '|'
str_val = str_val.join(['1', '2', '3', '4'])
print(str_val)
# ljust
str_val = 'TEST'
print(repr(str_val))
str_val = str_val.ljust(20)
print(repr(str_val))
# rjust
str_val = 'TEST'
str_val = str_val.rjust(20)
print(repr(str_val))
# lower
str_val = 'TEST'
print(str_val)
str_val = str_val.lower()
print(str_val)
# lstrip
str_val = '\n\t TEST'
print(str_val)
str_val = str_val.lstrip()
print(str_val)
# maketrans and translate
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
_str = "this is string example....wow!!!"
print(_str.translate(trantab))
# partition
str_val = 'lorem|ipsum|'
str_val = str_val.partition('|')
print(str_val)
str_val = 'lorem|ipsum|'
str_val = str_val.rpartition('|')
print(str_val)
# replace
str_val = 'lorem|ipsum'
str_val = str_val.replace('|', ',')
print(str_val)

# split
str_val = 'lorem|ipsum|foo|bar'
str_val = str_val.split('|')
print(str_val)
# rsplit
str_val = 'lorem|ipsum|foo|bar'
str_val = str_val.rsplit('|')
print(str_val)
# splitlines
str_val = 'lorem\nipsum\nfoo\nbar'
str_val = str_val.splitlines()
print(str_val)
# strip
str_val = '   Test   '
print(repr(str_val))
str_val = str_val.strip()
print(repr(str_val))
# swapcase
str_val = 'TesT'
str_val = str_val.swapcase()
print(str_val)
# title
str_val = 'TesT'
str_val = str_val.title()
print(str_val)
# upper
str_val = 'TesT'
str_val = str_val.upper()
print(str_val)
# zfill
str_val = '1'
str_val = str_val.zfill(10)
print(repr(str_val))
