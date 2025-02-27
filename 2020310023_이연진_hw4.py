import numpy as np

x = []
def desc_stat(*args):
    for arg in args:
        x.append(arg)
    return np.min(x), np.max(x), np.var(x), np.std(x), np.mean(x), np.median(x)

desc_stat(7, 4, 3, 9, 5)

a = np.random.choice(50, 100)

for i in range(100):
    if a[i] % 3 == 1:
        print(a[i])
    else:
        pass

a = np.random.rand(100000)
print(np.mean(a), np.std(a))

b = np.random.randn(100000)
print(np.mean(b), np.std(b))

x = np.array([1,2,3,3,4,5])
x[max(np.bincount(x))]

x = np.array([0,1,1,1,2,3,3,4,4,4,5])
x[max(np.bincount(x))]

players = [['김승규', '사우디', '알샤바브'], ['조현우', '한국', '울산현대'],
           ['김영권', '한국', '울산현대'], ['홍철', '한국', '대구FC'],
           ['손흥민', '영국', '토트넘'], ['이재성', '독일', '마인츠'],
           ['정우영', '카타르', '알사드'], ['황희찬', '영국', '울버햄튼']]


a = np.array(players)
idx1 = np.array(a[:, 1] == '한국')
a[idx1]

idx2 = np.array(a[:, 2] == '울산현대')
a[idx2]

