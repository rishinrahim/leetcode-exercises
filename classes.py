"""

Naming Conventions
-------------------------

Class names should normally use the CapWords convention.
Function names: lowercase with words separated by underscores as necessary to improve readability.

Documentation in  Python
-----------------------------
Python provides support for embedding formal documentation directly in source code
using a mechanism known as docstring

"""

class CreditCard:
    """ A consumer credit card"""

    def __init__(self,customer,bank,acnt,limit):
        """ create a credit card instance

        The intial balnce is zero

        customer the name of the customer
        bank     the name of the bank
        acnt     the account number
        limit    credit limit (measured in dollars)

        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0


    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_acnt(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def charge(self,price):

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        self._balance-=amount


if __name__ == "__main__":
    cc= CreditCard("john","citibank",20718,10000)
    print(cc.get_customer())