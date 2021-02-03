# Explains Inheritance and Polymorphism


class Customer(object):

    def __init__(self, name, account_no):
        self.name = name
        self.account_no = account_no

    def status(self):
        print(f'{self.name} has loan account')


class HomeLoan(Customer):

    def __init__(self, principal, rate, time, name, account_no):
        self.principal = principal
        self.rate = rate
        self.time = time

        # super function is used instead of class Customer and its reference to initialize parent class attributes
        # Customer.__init__( self, name, account_no)

        super().__init__( name, account_no)

    def interest(self):
        value_interest = self.principal * self.rate * self.time / 100
        return print(f'Interest for user {self.name} is : {value_interest}')

    def status(self): # function with name 'status' was also present in parent class
        print(f'{self.name} paying interest {self.rate}%')


user = Customer('Billy', 12345)
user.status()
hl = HomeLoan(1000, 10, 1, 'Tom', 1234)
hl.interest()
hl.status()
