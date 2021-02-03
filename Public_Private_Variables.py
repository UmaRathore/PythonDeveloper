# public and private variables

class HomeLoanPrivate:

    # The variables which need not to be altered, should have '_' in the beginning
    # so that system will know it shouldn't be changed (private variable)

    def __init__(self, principal, rate, time):
        self._principal = principal
        self._rate = rate
        self._time = time

    def interest(self):
        value_interest = self._principal * self._rate * self._time / 100
        print(f'Interest at default rate {self._rate}% is : {value_interest}')
        return


class HomeLoanPublic:

    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def interest(self):
        value_interest = self.principal * self.rate * self.time / 100
        print(f'Interest at new rate {self.rate}% is : {value_interest}')
        return

# try to override function outside the class 'HomeLoanPrivate' by modifying 'rate',
# Here 'rate' will NOT be modified as it is a private variable


new_rate = float(input('Enter Rate of interest other than default 10% : '))

hl_prv = HomeLoanPrivate(1000, 10, 1)
hl_prv.rate = new_rate
hl_prv.interest()

# try to override function outside the class 'HomeLoanPublic' by modifying 'rate',
# Here 'rate' (public variable) will be modified and function will be overridden with new value of 'rate'

hl_pub = HomeLoanPublic(1000, 10, 1)
hl_pub.rate = new_rate
hl_pub.interest()
