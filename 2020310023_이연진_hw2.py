heaven={'라면':[3500, 5], '김밥':[3000, 10], '우동':[5000, 7], '돈까스':[7000, 5]}

heaven2 = list(heaven.values())

heaven2

heaven={'라면':[3500, 5], '김밥':[3000, 10], '우동':[5000, 7], '돈까스':[7000, 5]}

heaven2 = list(heaven.values())

heaven2[0][0] + heaven2[1][0] + heaven2[2][0] + heaven2[3][0]



num=[[1,2],[3,4],[5,6]]

for i in num:
    for k in i:
        print(k, end = ' ')



for i in range(0,7,2):
    for j in range(0, 4):
        print(i+j, end = ' ')
    print(' ')



n = 5

for i in range(1, n+1):
    print(('*'*i) + ' '*(n-i) + ' '*(n-i) + ('*'*i))

for j in range(n-1, 0, -1):
    print(('*'*j) + ' '*(n-j) + ' '*(n-j) + ('*'*j))



def triple_one(a):
    result = []
    for n in a:
        if n % 3 == 1:
            result.append(n)
    return result

triple_one(a=[5,4,9,11,16])



