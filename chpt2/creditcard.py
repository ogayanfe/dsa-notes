from typing import Any


class CreditCard:

    """A consumer credit card."""

    def init (self, customer: str, bank: str, acnt: float, limit: float, balance: int | float = 0.0):
        """Create a new credit card instance.
        The initial balance is zero.
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance: float =   balance

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance
    
    def charge(self, price: float | int):
        if price + self._balance > self._limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount: Any):
        if not isinstance(amount, int) and not isinstance(amount, float): 
            raise ValueError(f'Value "{amount}" is not an instance of int | float')

        if amount < 0: 
            raise ValueError('Amount cannot be negative')

        self._balance -= amount

