import numpy as np

x = np.arange(3)
x

y = np.arange(5)
y

X, Y = np.meshgrid(x, y)

X

Y

[list(zip(x, y)) for x, y in zip(X, Y)]



import numpy as np
import time

x = np.arange(1, 10001)
y = np.arange(10001, 20001)

z = np.zeros_like(x)
start = time.time()
for i in range(10000):
    z[i] = x[i] + y[i]
end = time.time()

print(z[:10])
print('%.8f sec' %(end-start))



# Commented out IPython magic to ensure Python compatibility.
# %%time
# z = np.zeros_like(x)
# for i in range(10000):
#     z[i] = x[i] + y[i]

z[:10]



z = np.zeros_like(x)
start = time.time()
z = x + y
end = time.time()

print(z[:10])
print('%.8f sec' %(end-start))



# Commented out IPython magic to ensure Python compatibility.
# %%time
# z = x + y

z[:10]



a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])

a == b

a >= b



a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])

np.all(a == b)

np.all(a == c)

np.all(a != b)



a = np.arange(5)
a

np.exp(a)

10 ** a

np.log(a + 1)



x = np.arange(5)
x

y = np.ones_like(x)
y

x + y

x + 1



x = np.array([(0,1,2),(1,2,3),(2,3,4),(3,4,5),(4,5,6)])
y = np.array([0,1,2,3,4])
yt = y.reshape(5,1)

print(x)
print(y)
print(yt)
print(x+yt)

x = np.arange(15).reshape(5,3)
y = np.arange(5)
yt = y.reshape(5,1)

print(x)
print(y)
print(yt)
print(x+yt)



x = np.array([1, 2, 3, 4])

np.sum(x)
np.min(x)
np.max(x)
np.argmin(x)
np.argmax(x)
np.mean(x)
np.median(x)



x = np.array([True, True, False])
print(np.all(x))
print(np.any(x))

y = np.array([True, True, True, True])
print(np.all(y))
print(np.any(y))

z = np.array([False, False, False])
print(np.all(z))
print(np.any(z))



a = np.zeros((100, 100), dtype=np.int)
a

np.any(a != 0)

np.all(a == a)



x = np.arange(24)
x = x.reshape(2,3,4)
print(x)

print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
print(np.sum(x, axis=2))





x = np.arange(8,68,2)
x = x.reshape(5,6)
print(x)

np.max(x)

x.sum(axis=1)
np.sum(x, axis=1)

x.max(axis=1)
np.max(x, axis=1)

x.mean(axis=0)
np.mean(x, axis=0)

x.min(axis=0)
np.min(x, axis=0)



