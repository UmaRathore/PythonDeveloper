# Functions

def student_registration():
    scholar_name = input("Student name: ")
    student_class = input("Enrollment class : ")
    print(f'Name : {scholar_name} Class : {student_class}')


student_registration()


# Parameters and Arguments and Default Parameters

def student_registration(name='Student', age=None):
    print(f'Name : {name} Age : {age}')


student_name = input("Student name: ")
student_age = input("Student Age : ")
student_registration(student_name, student_age)
student_registration()


# Return
def func_sum(num1, num2):
    """
    msg: function about addition
    """

    def func_add(n1, n2):
        print('hello')
        return n1 + n2

    return func_add(num1, num2)


total = func_sum(10, 20)
print(total)

help(func_sum)
print(func_sum.__doc__)


# Exercise - Check drivers age

# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get
# prompted for age. Notice the benefit in having checkDriverAge() instead of copying and pasting the function
# everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you
# enter: checkDriverAge(92); it returns "Powering On. Enjoy the ride!" also make it so that the default age is set to
# 0 if no argument is given.

def checkDriverAge(age):
    # age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(12)


# *args and **kwargs

def sample_func(*args):
    print(*args)


sample_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sample_func(1, 2, 3, 4, 5)


def sample_func(*args):
    print(args)
    return sum(args)


print(sample_func(1, 2, 3, 4, 5))


def sample_func(**kwargs):
    add_numbers = 0
    print(kwargs)
    for items in kwargs.values():
        add_numbers += items
    return add_numbers


print(sample_func(num1=1, num2=2, num3=3))


# Exercise : Function to find highest even number

def highest_even_number(*args):
    even_numbers = []
    for items in args:
        if items % 2 == 0:
            even_numbers.append(items)
    even_numbers.sort()
    even_numbers.reverse()
    return even_numbers[0]


print(highest_even_number(10, 2, 3, 4, 8, 11))

# Walrus Operator

sample_list = [1, 2, 3, 4, 5]
if (number_count := len(sample_list)) > 1:
    print(f'list has {number_count} numbers')
