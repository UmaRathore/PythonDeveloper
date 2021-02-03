# Fundamental Data Types

2 + 3  # acton is not defined here thus it is not executed, no result on terminal
print('Data Type of Two numbers:')
print(type(2 + 3))  # here action is defined by print() function thus value is returned and printed on screen
print(type(2 / 4))  # type is case sensitive
print('Multiplication of 2 and 3:')
print(2 * 3)
print('3 to the power of 2:')
print(2 ** 3)
print(2 ** 3)  # space makes no difference
print('Value return by // is integer 2//4:')
print(2 // 4)  # return integer, here it return zero
print('Value return by // is integer 5//4:')
print(5 // 4)  # here it return 1
print('Mod function 5%4')
print(5 % 4)  # prints remainder

# Operator precedence
print('Operator precedence 30-4*3')
print(30 - 4 * 3)

# Functions
print('Binary number of 5')
print(bin(5))  # O/P has 0b means it is a binary number
print('integer to a binary number')
print(int('0b101', 2))  # here return int value of '0b101' which is a base 2 value

# Variables to store information in memory
print('Variable assignment and their values')
num = 10
print(num)

length, breadth, height = 3, 4, 5
print(length)
print(breadth)
print(height)

# Augmented Assignment Operator
print('Augmented Operator')
number = 2
number += 4  # instead of number = number + 3
print(number)

# String
print('Hello World - Data')
print(type('hello world'))
long_string = '''
WWWWW
0   0
  0
-----
MMMMM
'''
print(long_string)

# String Concatenation
first_name = 'Uma'
last_name = 'Rathore'
print('Example of string concatenation')
print(first_name + ' ' + last_name)

# Type Conversion
print('Example of type Conversion from int to str')
print(type(str(10)))

# Escape Sequence
print("Hello \'Machine Learning\' community")

# Formatted String
name = 'Uma'
role = 'Manager'
print(f'Hello {name}, Good Morning. Your role is  {role}')
print('Hello {}, Good Morning. Your role is {}'.format(name, role))
