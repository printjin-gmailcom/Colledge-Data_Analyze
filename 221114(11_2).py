import numpy as np

ar = np.array([0,1,2,3,4])
print(ar)
ar

print(type(ar))
type(ar)



num = [0,1,2,3,4]

result = []
for i in num:
    result.append(2*i)

print(result)

num = [0,1,2,3,4]

print(num*2)

ar = np.array([0,1,2,3,4])
ar = ar*2
print(ar)



a = np.array([0,1,2])
b = np.array([2,4,6])

print(2*a+b)
print(a==2)
print((a==1)&(b>3))

a = np.array([0,1,2])
b = np.array([2,4,6,8])

a+b



na = np.array([[0,1,2],[3,4,5]])

print(na)
print(len(na))
print(len(na[0]))

na = np.array([[0,1,2],[3,4,5,6]])

print(na)



nb = np.array([[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]],
              [[11, 12, 13, 14],[15, 16, 17, 18],[19, 20, 21, 22]]])

print(nb)
print(len(nb), len(nb[0]), len(nb[0][0]))
print(nb.ndim) #차원
print(nb.shape) #깊이가 2개, 행이 3개. 열이 2개



nc = np.array([[10,20,30,40],[50,60,70,80]])

print(nc)
print(nc.ndim)
print(nc.shape)



import numpy as np

a = np.array([0, 1, 2, 3, 4])

a[2]
a[-1]

a = np.array([[0, 1, 2], [3, 4, 5]])

a[0,0]
a[0,1]
a[1,0]
a[-1,0]
a[-1,-1]

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

a[0, :]  # 첫번째 행 전체
a[:, 1]  # 두번째 열 전체
a[1, 1:]  # 두번째 행의 두번째 열부터 끝열까지
a[:2, :2]

a = np.array([[ 0,  1,  2,  3],[4, 5, 6, 7],[8, 9, 10, 11]])

print(a[0,1:3])
print(a[1:3,0])
print(a[0:2][0:2])
print(a[1,:])
print(a[:,2])
print(a[:,:])

a = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])

a[1,2]
a[-1,-1]
a[1,1:3]
a[1:,2]
a[:2,3:]



a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True,
               False, True, False, True, False])
a[idx]

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a % 2

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a % 2 ==  0

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[a % 2 == 0]

a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
a[idx]

a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
a[idx]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a
a[:, [True, False, False, True]]
a[[2, 0, 1], :]



a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

idx = a%3 ==0
print(a[idx])

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

idx = a%4 == 1
print(a[idx])

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

idx = (a%3 ==0) & (a%4 == 1)
print(a[idx])

