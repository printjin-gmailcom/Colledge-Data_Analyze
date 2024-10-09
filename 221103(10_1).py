class Account:
    def __init__(self, bank, name, balance):
        self.bank  = bank
        self.name = name
        self.balance = balance
    def deposit(self, a):
        if a >= 1:
            self.balance += a
        else:
            print('error')
    def withdraw(self, a):
        if a > 1 and self.balance >= a :
            self.balance -= a
        else:
            print('error')

money = Account('국민', '홍길동', 40000)
money.withdraw(1)
money.withdraw(10000)
print(money.balance)

class Account:
    def __init__(self, bank, name, balance):
        self.bank  = bank
        self.name = name
        self.balance = balance
    def deposit(self, a):
        if a >= 1:
            self.balance += a
        else:
            print('error')
    def withdraw(self, a):
        if a > 1 and self.balance >= a :
            self.balance -= a
        else:
            print('error')
    def display(self):
        print('은행명:',self.bank)
        print('예금주:', self.name)
        print('잔액:', self.balance)


money = Account('국민', '홍길동', 40000)
money.display()

class InAccount(Account):
    def deposit(self, a):
        if a >= 1:
            self.balance += a
            self.balance = int(1.01*self.balance)
        else:
            print('error')


money = InAccount('국민', '홍길동', 40000)
money.deposit(1000)
print(money.balance)



