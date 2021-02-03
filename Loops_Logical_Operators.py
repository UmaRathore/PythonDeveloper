# If Else and Truthy Falsey values

username = 'uma'
password = '12345'

print(f'value of username : {bool(username)} {bool(password)}')
print(f'value for none : {bool(None)} value for blank string {bool("")}')

if username and password:
    print('login successful')
else:
    print('register first')

# Ternary Operator / generally sed ot write clean coide with less lines

is_friend = True
print("Allow Message") if is_friend else print("Not Allowed")

# Short Circuiting / use of OR operator

is_low_income = True
is_passed_exam = True

if is_low_income or is_passed_exam:
    print('scholarship granted')

# Exercise : Logical Operators

is_magician = True
is_expert = False

if is_magician and is_expert:
    print('you are master magician')
elif is_magician and not is_expert:
    print('atleast you are getting there')
else:
    print('you need magic powers')

# IS vs ==

print(True == 1)
print(True is 1)
print([] == [])
print([] is [])

# For Loop

for items in (1, 2, 3, 4, 5):
    for data in ['a', 'b']:
        print(items, data)

for items in 'hello':
    print(items)

# Exercise : Counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for items in my_list:
    counter = counter + items
print(counter)

# Range

for number in range(10):
    print(number)

for _ in range(0, 5):
    print(_)

for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -1):
    print(_)

for _ in range(2):
    print(list(range(5)))

# Enumerate()

for i, char in enumerate('Hello'):
    print(i, char)

for i, number in enumerate([11, 12, 13, 14, 15]):
    print(i, number)

# index of number 50 in list
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i)

# while Loop

i = 0
while i < 5:
    print(i)
    i += 1
    print('while loop breaked')
    break
else:
    print('while loop closed with an else')

while True:
    username = input('Username : ')
    if username == '':
        break

# Exercise : Print a Christmas Tree from given list

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# Append values in a list using iteration

shapes = []
num = 0
j = 0
while j < 4:
    shapes.append(num)
    j += 1
    num += 1
print(shapes)

# Christmas tree code 1

i = 0
treeimage = []
while i < len(picture):
    for item in picture[i]:
        if item == 0:
            treeimage.append(' ')
        else:
            treeimage.append('*')
    print(treeimage)
    treeimage.clear()
    i += 1

# Christmas tree code 2

for item in picture:
    for image in item:
        if image == 0:
            print(' ', end='')
        if image == 1:
            print('*', end='')
    print('')

# Christmas tree code 3
fill = '*'
empty = ' '
for item in picture:
    for image in item:
        if (image):
            print(fill, end='')
        else:
            print(empty, end='')
    print('')

# Exercise : Check for duplicate values

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)
