class Account():
    def __init__(self, owner, balance):
        self.owner =owner
        self.balance =balance

    def __str__(self):
        return (f'Owner: {self.owner}\nBalance: {self.balance}')

    def __balance__(self):
        return self.balance()

    def __owner__(self):
        return self.owner()

    def deposit(self, dcash):
        self.balance+=dcash
        print('Deposit Accepted!')
        print(f'New balance amt is {self.balance}')

    def withdraw(self, wcash):
        if wcash>self.balance:
            print('Unavailable Funds!')
        else:
            self.balance-=wcash
            print('Withdrawl Accepted!')
            print(f'New balance amt is {self.balance}')
