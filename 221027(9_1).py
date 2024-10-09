class Singer:
    def sing(self):
        return 'doremi'


IU = Singer()
print(IU.sing())

IVE = Singer()
print(IU.sing())



result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
print(add(5))

result2 = 0
def add2(num):
    global result2
    result2 += num
    return result2

print(add2(3))
print(add2(5))
print(add2(7))

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal1.add(5))
print(cal2.add(3))
print(cal2.add(5))
print(cal2.add(7))





class FourCal :
    pass

a = FourCal()
print(a)

class FourCal :
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2)

print(a.first)
print(a.second)

# setdata(self, first, second)
# self.X(first,second)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a  = FourCal()
b  = FourCal()
a.setdata(4,2)
b.setdata(3,5)

print(a.add())
print(b.add())

class FourCal:
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

a  = FourCal()
b  = FourCal()
c  = FourCal()
d  = FourCal()

a.setdata(4,2)
b.setdata(3,5)
c.setdata(8,6)
d.setdata(7,9)


print(a.add())
print(b.mul())
print(c.sub())
print(d.div())

