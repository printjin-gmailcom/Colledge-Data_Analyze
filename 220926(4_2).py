a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)

a = 0
while a < 10:
    print(a)



test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (x, y) in a:
    print(x + y)

a = [(1,2), (4,5), (7,8)]
for (x, y) in a:
    print(x * y)



score = [90, 25, 67, 45, 80]
number = 0

for i in score:
    number += 1
    if i >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)



a = range(10)
a

a = range(10)
type(a)



add = 0
for i in range(1, 11):
    add = add + i

print(add)



for i in range(5):
    print(i)



for i in range(2,10):
    for j in range(1, 10):
        print(i*j)
    print('=======')

for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end = ' ')
    print('')



a = [1,2,3,4]
result = []

for num in a:
    result.append(num*3)

print(result)

a = [1,2,3,4]
result = [num * 3 for num in a]

print(result)



result = [x*y for x in range(2,10)
    for y in range(1,10)]

print(result)



a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

a = range(8)
result = [num * 3 for num in a if num % 2 == 0]
print(result)



result = [i*j for i in range(2,10)
         for j in range(1,10)]
result





a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

a = range(1, 100)
result1 = [num * 3 for num in a if num % 2 == 0]





h = 0
j = 0
a = range(1,101)

for i in a:
    if i%2 == 0:
        j += i
    else:
        h += i

print(h)
print(j)





for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end = ' ')
    print('')

a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)







