import numpy as np

a = np.array([1,2,3])
a.dtype

x = np.array([1.0, 2.0, 3.0])
x.dtype

c = np.array([1,2,3.0])
c.dtype



dtype 접두사

b 불리언 b (참 혹은 거짓)

i 정수 i8 (64비트)

u 부호 없는 정수 u8 (64비트)

f 부동소수점 f8 (64비트)

c 복소 부동소수점 c16 (128비트)

O 객체 0 (객체에 대한 포인터)

S 바이트 문자열 S24 (24 글자)

U 유니코드 문자열 U24 (24 유니코드 글자)

x = np.array([1, 2, 3], dtype='f') #f2. f4. f8 변경 가능
x.dtype
x[0] + x[1]

x = np.array([1, 2, 3], dtype='i2') #i2 등 변경 가능
x.dtype
x[0] + x[1]

x = np.array([1, 2, 3], dtype='U')
x.dtype
x[0] + x[1]



print(np.inf)
print(np.nan)

a = np.array([0, 1, -1, 0])
b = np.array([1, 0, 0, 0])

print(a/b)
print(np.log(0))

np.exp(-np.inf)



a = np.zeros(5)
a

b = np.zeros((2, 3))
b

c = np.zeros((5, 2), dtype="i")
c

d = np.zeros(5, dtype="U4")
d

d[0] = "abc"
d[1] = "abcd"
d[2] = "ABCDE"
d

e = np.ones((2, 3, 4), dtype="i8")
e

f = np.ones_like(b, dtype="f")
f

g = np.empty((4, 3))
g

np.arange(10)  # 0 .. n-1

np.arange(3, 21, 2)  # 시작, 끝(포함하지 않음), 단계

np.linspace(0, 100, 5)  # 시작, 끝(포함), 갯수

np.logspace(0.1, 1, 10)



A = np.array([[1, 2, 3], [4, 5, 6]])
A

A.T



a = np.arange(12)
a

b = a.reshape(3, 4)
b

a.reshape(3, -1)

a.reshape(2, 2, -1)

a.reshape(2, -1, 2)

a.flatten() #다차원 배열을 무조건 1차원으로 만들기 위해서

a.ravel() #다차원 배열을 무조건 1차원으로 만들기 위해서

x = np.arange(5)
x

x.reshape(1, 5)

x.reshape(5,1)

x[:, np.newaxis]



x = np.arange(5)

print(x)

print(x.reshape(1,5))

print(x.reshape(5,1))



a1 = np.ones((2, 3))
a1

a2 = np.zeros((2, 2))
a2

np.hstack([a1, a2])

b1 = np.ones((2, 3))
b1

b2 = np.zeros((3, 3))
b2

b2 = np.zeros((3, 3))

c1 = np.ones((3, 4))
c1

c2 = np.ones((3, 4))
c2

np.dstack([c1, c2])

(np.dstack([c1, c2])).shape

c = np.stack([c1, c2])
c

c.shape

c = np.stack([c1, c2], axis=1)
c

c.shape

np.r_[np.array([1, 2, 3]), np.array([4, 5, 6])]

np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])]

a = np.array([[0, 1, 2], [3, 4, 5]])
np.tile(a, 2)

np.tile(a, (3, 2))



a = np.r_[np.zeros(3), np.ones(2)]
b = np.tile(a, (3,1))
c = np.linspace(10, 150, 15).reshape(-1, 5)
d = np.vstack([b, c])
e = np.tile(d, (2,1))
print(e)

