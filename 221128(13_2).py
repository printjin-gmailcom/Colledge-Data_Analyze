import numpy as np

np.random.choice(5, 4)

print(np.random.choice(5, 5, replace=False))
print(np.random.choice(5, 3, replace=False))
print(np.random.choice(2, 3, replace=False))

np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0])



np.random.choice(2, 10, p=[0.5, 0.5])

np.mean(np.random.randint(1, 7, 100))

price = 10000
price_list = []
for i in range(250):
    price = price*(1+np.random.randn()*0.01)
    price_list.append(int(price))
print(price_list)

import matplotlib.pyplot as plt
plt.plot(price_list)
plt.show()



np.unique([11, 11, 2, 2, 34, 34])

a = np.array(['a', 'b', 'b', 'c', 'a'])
index, count = np.unique(a, return_counts=True)
index, count

np.bincount([1, 1, 2, 2, 2, 3], minlength=6)

