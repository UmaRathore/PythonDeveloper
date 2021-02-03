# Methods Resolution Order

class Customer:

    def __init__(self, name):
        self.name = name


class HomeLoan(Customer):

    def __init__(self, name):
        Customer.__init__(self, name)


class Interest(Customer):

    def __init__(self, rate, name):
        Customer.__init__(self, name)
        self.rate = rate


class LoanStatus(Interest, HomeLoan):

    def __init__(self, name, rate):
        Interest.__init__(self, rate)
        HomeLoan.__init__(self, name)

# this method will print the sequence of the classes caleed during execution


print(LoanStatus.mro())
