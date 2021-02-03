# this code explains the concept of class methods and static methods

class HomeLoan:

    def __init__(self, current_amount, loan_capacity):
        self.current_amount = current_amount
        self.loan_capacity = loan_capacity
        print(f'Amount is : {current_amount}')
        print(f'Loan Capacity is : {loan_capacity}')

    def loan_status(self):
        if self.current_amount == self.loan_capacity:
            print('loan is closed')
        else:
            print('loan is active')

    # class methods has class reference

    @classmethod
    def loan_amount(cls, principal, rate, time):
        return cls(principal + principal * rate * time / 100, 5000)

    # Static methods has no class reference

    @staticmethod
    def interest(principal, rate, time):
        value_interest = principal * rate * time / 100
        return print(f'Interest is : {value_interest}')


# class methods and static methods can be instantiated without instantiating objects

HomeLoan.loan_amount(1000, 10, 1)
HomeLoan.interest(1000, 10, 1)
