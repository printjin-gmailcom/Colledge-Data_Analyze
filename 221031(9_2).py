class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a=FourCal()
b=FourCal()

a.setdata(4,2)
b.setdata(5,3)



class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a=FourCal(4,2)
b=FourCal(5,3)

print(a.add())
print(a.mul())
print(b.sub())
print(b.div())



class MoreFourCal(FourCal):
    pass


a=MoreFourCal(6,4)
b=FourCal(7,5)

print(a.add())
print(a.mul())
print(b.sub())
print(b.div())



class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a=MoreFourCal(8,6)

print(a.pow())

b=FourCal(9,7)

print(b.pow())



class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 0)
a.div()



class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
a.div()



class Singer:
    sing = 'doremi'

IU =  Singer()
IVE = Singer()

print(IU.sing)
print(IVE.sing)

Singer.sing = 'fasollasi'

print(IU.sing)
print(IVE.sing)





class Account:
    def __init__(self, bank, name, balance):
        self.bank  = bank
        self.name = name
        self.balance = balance

money = Account('국민', '홍길동', 40000)

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

money = Account('국민', '홍길동', 40000)
money.deposit(1000)
print(money.balance)







