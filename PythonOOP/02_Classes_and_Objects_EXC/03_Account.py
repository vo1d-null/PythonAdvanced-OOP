class Account:
    # initialize the account with id, name and balance
    def __init__(self, id, name: str, balance=0):
        self.id = id
        self.name: str = name
        self.balance = balance

    # add credit to the account and return the updated balance
    def credit(self, amount):
        self.balance += amount
        return self.balance

    # deduct debit from the account and return the updated balance
    # if the amount is more than the balance, return "Amount exceeded balance"
    def debit(self, amount):
        if amount > self.balance:
            return "Amount exceeded balance"
        self.balance -= amount
        return self.balance

    # return the account information in a formatted string
    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


# create an account object with id and name
account = Account(5411256, "Peter")
# perform debit, credit and debit operations on the account and print the updated balance
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
# print the account information
print(account.info())
