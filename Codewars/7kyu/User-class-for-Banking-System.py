"""
Description:
A company is opening a bank, but the coder who is designing the user class is having trouble. They need you to help them.

Task
Implement the following methods on the User class (the initial class structure has already been prepared for you)

- withdraw(self, amount)
    Subtracts amount from the user's balance
    Raises a ValueError if there isn't enough balance to withdraw amount (overdraw)
    Otherwise returns the string "<Name> has <balance>.", with the user's name and new balance, respectively.

- check(self, issuer, amount)
    Transfers amount from issuer to the user
    issuer will always be a valid User
    Raises a ValueError if issuer does not have the balance to cover the amount (bad check)
    Raises a ValueError if issuer's checking_account attribute is False (non-checking account)
    Otherwise returns the string "<User name> has <user balance> and <Issuer name> has <issuer balance>.", with the user's and issuer's names and new balances, respectively.

- add_cash(self, amount)
    Adds amount to the user's balance
    Returns the string "<Name> has <balance>.", with the user's name and new balance, respectively.

Notes
    - The boolean attribute checking_account must exist on the class
    - Numeric inputs will be non-negative integers, balance should always be an integer.
    - Output strings must end with a period
    - No currency will be used

Examples:
    Jeff = User(name='Jeff', balance=70, checking_account=True)
    Joe  = User(name='Joe',  balance=70, checking_account=False)

    Jeff.withdraw(2) # Returns 'Jeff has 68.'

    Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

    Jeff.check(Joe, 80) # Raises a ValueError (Joe is not a checking account)

    Joe.checking_account = True # Enables checking for Joe

    Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

    Joe.check(Jeff, 100) # Raises a ValueError (bad check)

    Jeff.add_cash(20.00) # Returns 'Jeff has 118.'
"""

class User:
    
    def __init__(self, name: str, balance: int, checking_account: bool):
        # the account holder's name
        self.name = name
        # the initial balance
        self.balance = balance
        # whether this user can issue checks to others
        self.checking_account = checking_account
    
    def output(self):
        return "{} has {:d}.".format(self.name, self.balance)
        
    def withdraw(self, amount):
        """Withdraw `amount` from this account, if balance is sufficient"""
        if self.balance < amount: 
            raise ValueError("overdraw")
            
        self.balance -= amount
        return self.output()
    
    def add_cash(self, amount):
        """Deposit `amount` into this account"""
        self.balance += amount
        return self.output()
    
    def check(self, issuer, amount):
        """Receive a check from `issuer` over `amount`, if possible
        
        `issuer` is the User issuing the check, i.e. the account the `amount` will be taken from
        `self` is the User receiving the check, i.e. the account the `amount` will be added to
        """
        if not issuer.checking_account:
            raise ValueError("Joe is not a checking account")
        
        if issuer.balance < amount:
            raise ValueError("bad check")
        
        issuer.withdraw(amount)
        self.add_cash(amount)
        
        return f"{self.name} has {self.balance} and {issuer.name} has {issuer.balance}."