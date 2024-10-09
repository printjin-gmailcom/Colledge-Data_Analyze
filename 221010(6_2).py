def add(a, b):
    return a + b

a=3
b=5
c=add(a,b)
c

add(3,5)

add('ab','cd')

add([1,2],[3,4])



def multi(a,b):
    return a*b

c= multi(3,5)
c

def func1(a,b):
    return f'{a}*{b}={a*b}'

def func2(a,b):
    return a+b, a*b

def func3(a,b):
    return [a+b, a*b]

type(func1(3,5))

type(func2(3,5))

type(func3(3,5))

def func(a, b):
    return a + b
    return a * b

func(3,5)

def hello():
    return 'Hello'

a= hello()

a



def num(a,b):
    print(f'{a}. {b}')

c=num(3,5)

c

type(c)



def hello():
    print('Hello')

a=hello()

print(a)



def func(a,b):
    return 'a=%d, b=%d, a+b=%d' %(a,b,a+b)

func(3,5)

func(a=3,b=5)

func(b=5, a=3)



def add(*args):
    result=0
    for i in args:
        result += i
    return result

add(2,4,6)

add(1,2,3,4,5,6,7,8)



def func(a,b):
    if a+b > 10:
        return
    print(a+b)

func(3,4)

a = func(6,7)
a, type(a)



def func(a,b,c=5):
    return a+b+c

func(3,4)

func(3,4,7)

func(3,4, 5)

func(3,4,c=7)



def func(a,b=5, c):
    return a+b+c



a = 1
def func(a):
    a+=10
func(a) # 이건 11
print(a) # 이건 1

a = 1
def func(b):
    b+=10
func(a)
print(a)



def func(a):
    a = 1
    a+=10
func(a)
print(a)

a = 1
def func(a):
    a+=10
    return a
a=func(a)
print(a)

a = 1
def func():
    global a
    a+=10
func()
print(a)



add = lambda a,b : a+b
add(3,5)

def add(a,b):
    return a+b
add(3,5)



def coin():
    return 'doge'

for i in range(10):
    print(coin())

def coin():
    print('doge')

for i in range(10):
    coin()



