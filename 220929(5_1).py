i = 4
while i < 7:
    j = 0
    while j < 9:
        j += 1
        print(f'{i} * {j} = {i*j}')
    i += 1
    print(' ')





for i in range(4,7):
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)
    print(' ')

for i in range(4,7):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print(' ')

for i in range(4,7):
    for j in range(1, 10):
        print('%d * %d = %d' %(i, j,i*j))
    print(' ')





scores = [100, 75, 90, 50, 85]
grade = [ ]

for score in scores:
    if score >= 90:
        grade.append( "A" )
    elif score >= 80:
        grade.append( "B" )
    elif score >= 70:
        grade.append( "C" )
    else:
        grade.append( "F" )
grade



score = [100, 75, 90, 50, 85]
grade = [ ]
i= 0
while i < len(score):
    if score[i] >= 90:
        grade.append( "A" )
    elif score[i] >= 80:
        grade.append( "B" )
    elif score[i] >= 70:
        grade.append( "C" )
    else:
        grade.append( "F" )
    i += 1
grade





a = ['starbucks', 'twosomeplace','hollys','megacoffee']

for i in a:
    print(len(i))



a = ['starbucks', 'twosomeplace','hollys','megacoffee']
i = 0
while i > len(a):
    print(len(a[i]))
    i += 1





a = ['starbucks', 'twosomeplace','hollys','megacoffee']

for i in a:
    print(i, len(i))





a = ['hello.py', 'HW1.hwp', 'python.docx']

for i in a:
    print(i.split('.')[0])





for i in range(11):
    print(10-i, end=' ')



