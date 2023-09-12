from BankAccount import BankAccount

if __name__ == "__main__":
    account = BankAccount("1190032233", 881.91)
    print(account.get_balance())
    account.deposit(18.09)
    print(account.get_balance())
    account.withdraw(900)
    print(account.get_balance())