# INFO
# Austin Fraley 801129991
# 09/10/2023


class BankAccount:
    
    """
    Class to store checking account information
    """

    def __init__(self, account_name=None, starting_balance=None):

        """
        Default constructor
        """

        self.account_name = account_name
        self.balance = starting_balance

    def get_balance(self):

        """
        Method to return a string containing the bank account balance
        """

        return f"{self.account_name} has a balance of {self.balance}"

    def deposit(self, amount):

        """
        Method to deposit money into bank account
        """

        self.balance += amount

        return None

    def withdraw(self, amount):
        
        """
        Method to withdraw money from the bank account
        """

        self.balance -= amount

        return None
