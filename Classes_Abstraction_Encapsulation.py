# HomeLoan Class to calculate loan amount and check its status
# this class explains concept of objects and self reference.


# Encapsulation : creating a class to bind attributes and functions.
# It can be used as objects to access its functionalities


class HomeLoan:

    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def interest(self):
        value_interest = self.principal * self.rate * self.time / 100
        return print(f'Interest is : {value_interest}')


hl = HomeLoan(1000, 10, 1)

# Abstraction : hiding the details of how interest is calculated.

hl.interest()


