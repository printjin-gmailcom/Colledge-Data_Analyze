# for 단일문

for i in range(1,8):
    print('*' * i)

# while 단일문

i = 0
while i < 7:
    i = i + 1
    print( i * '*')



# for 단일문

n = 7
for i in range(n):
    print('*' * (i+1))

# while 단일문

n = 7
i = 0

while i < n:
    print('*' * (i+1))
    i +=1

# for 중첩문

n = 7
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

# while 중첩문

n = 7
i = 0

while i < n:
    j = 0
    while j < i + 1:
        print('*', end='')
        j += 1
    i +=1
    print()



# for 단일문

n = 6
for i in range(n, 0, -1):
    print('*' * (i+1))

# for 단일문

n = 7
for i in range(n):
    print('*' * (7-i))

# while 단일문

n = 7
i = 0

while i < n:
    print('*' * (n -i))
    i +=1

# while 단일문

n = 7
i = 0

while i < n:
    print('*' * (7-i))
    i +=1

# for 중첩문

n = 8
for i in range(8, 1, -1):
    for j in range(i-1):
        print('*', end='')
    print()

# for 중첩문

n = 7
for i in range(n):
    for j in range(7-i):
        print('*', end='')
    print()

# while 중첩문

n = 7
i = 0

while i < n:
    j = 0
    while j < 7 - i:
        print('*', end='')
        j += 1
    i +=1
    print()



# for 단일문

n = 7
for i in range(n):
    print(' ' *(n-i) + '*' * (i+1))

# while 단일문

n = 7
i = 0

while i < n:
    print(' ' * (n-i) + '*' * (i+1))
    i +=1

# for 중첩문

n = 7
for i in range(n):
    for j in range(n-1-i):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()

# while 중첩문



# for 단일문

n = 7
for i in range(n):
    print(' ' * i + '*' * (7-i))

# while 단일문

n = 7
i = 0

while i < n:
    print(' ' * i + '*' * (7-i))
    i +=1

# for 중첩문

n = 8
for i in range(n):
    for j in range(i + 1):
        print(' ', end='')
    for k in range(n-1-i):
        print('*', end='')
    print()

# while 중첩문











# for 단일문

n = 6
for i in range(1, n):
    if n % 2 == 0:
        pass
    print(" "*(n-i), "*"*(2*i-1))

# for 단일문

n = 5

for i in range(n):

    print(' '*(n-i-1)+'*'*(2*i+1))

# while 단일문

n = 6
i= 1

while i < n:
    print(' ' * (n-i) + '*' * (i*2-1))
    i +=1

# for 중첩문

n = 5

for i in range(n):

    for j in range(n-1-i):

        print(' ', end='')

    for k in range(2*i+1):

        print('*', end='')

    print()

# while 중첩문

# for 단일문

n = 5

for i in range(n):

    print(' '*(n-i-1)+'*'*(2*i+1))

for i in range(n-i):

    print(' '*(i+1)+'*'*(2*(n-i)-3))

# for 중첩문

n = 5

for i in range(n):

    for j in range(n-1-i):

        print(' ', end='')

    for k in range(2*i+1):

        print('*', end='')

    print()

for i in range(n-1):

    for j in range(i+1):

        print(' ', end='')

    for k in range(2*(n-i)-3):

        print('*', end='')

    print()

# for 단일문

n = 5

for i in range(n):

    print(' '*i+'*'*(2*(n-i)-1))

for i in range(n-i):

    print(' '*(n-i-2)+'*'*(2*i+3))

# for 중첩문

n = 5

for i in range(n):

    for j in range(i):

        print(' ', end='')

    for k in range(2*(n-i)-1):

        print('*', end='')

    print()

for i in range(n-1):

    for j in range(n-i-2):

        print(' ', end='')

    for k in range(2*i+3):

        print('*', end='')

    print()

