# program to get input from user for DOB and print age

birth_year = input('Year of birth : ')
age = 2021 - int(birth_year)
print(f'Your age is {age}')

# program to get username and password from user and print username password as * and display the length of password

user_name = input('Enter user name : ')
password = input('Enter password : ')
hidden_password = len(password) * '*'
print(f'{user_name} your password is {hidden_password} with length : {len(password)}')

# list methods

# adding

list_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
new_list = list_sample.append(10)
print(f'list has values : {list_sample}')
print(f'new list : {new_list}')
list_sample.extend([11])
print(list_sample)

# removing
list_sample.remove(9)
print(list_sample.pop())
print(list_sample)

print(F'Count of 1 in the list : {list_sample.count(1)}')
print(f'Is 2 present in the given list : {2 in list_sample}')

# List Unpacking, can be used to slice the list

var1, var2, var3, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(var1)
print(var2)
print(var3)
print(other)

# Dictionary, keys has to immutable, String, Integer or Boolean

User = {
    'name': 'Uma',
    'age': 26,
    'Married': True,
    '[10]': 'number',
    123: 'hello'
}

print(User['age'])
print(User[123])

# Dictionary methods

print(User.get('address'))  # to get value instead of error, use methods to return None
print(User.get('address', 'USA'))  # creates the key value pair if it doesnt exist

print('name' in User.keys())
print('number' in User.values())
print(User.items())

User_new = User.copy()
print(User_new)

User_new.clear()
print(User_new)

# Tuples, immutable list are Tuples

tuple_sample = (1, 2, 3, 4, 5)
print(tuple_sample)
new_tuple = tuple_sample[1:3]
print(new_tuple)
print(tuple_sample + new_tuple)
print(tuple_sample.count(1))
print(tuple_sample.index(1))
tup1, tup2, *other_tuple = (1, 2, 3, 4, 5, 6, 7)
print(tup1)
print(tup2)
print(other_tuple)

# set : point to unique values

set_sample = {1, 2, 3, 4, 5, 6, 6}
print(set_sample)  # print unique values
set_sample.add(10)
set_sample.add(2)  # add unique values in the list, thus 2 will not be added
print(set_sample)

# to sort a list set function is used

list_sample = [11, 12, 13, 14, 15, 15]
print(set(list_sample))
print(11 in list_sample)
print(len(set_sample))

print(set_sample)
print(list(set_sample))

set_one = {1, 2, 3, 4, 5, 6, 7, 8}
set_two = {6, 7, 8, 9, 10}
print(set_one.intersection(set_two))
print(set_one.issubset(set_two))
print(set_one.issuperset(set_two))
print(set_one.isdisjoint(set_two))
print(set_one.difference(set_two))
print(set_one.difference_update(set_two))
print(set_one)
print(set_one.discard(2))
print(set_one)
