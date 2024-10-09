a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

a,b,c,d,e

b = [1, 2, 3]

b[-1]
b[0]+b[-2]
type(b)
type(b[2])

e = [1, 2, ['Life', 'is']]

e[2][1]
type(e)
type(e[0])
type(e[-1])

f = [1, 2, ['a', 'b', ['Life', 'is']]]

f
f[2]
f[2][2][0]
f[-1][-1][-1]
type(f[2][2][0])

g = [1, 2, 3, 4, 5]

g[2:]

h = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

h[2:5]
h[3][:2]



i = [1,2,3,4,1,2,3,4]

i[2:5]



b = [1, 2, 3]
j = [4, 5, 6]

b + j
b * 3
len(b)

k = [1,[1,2,3,4,5,]]

len(k)
k[1]
len(k[1])

b = [1, 2, 3]

b[2] + "hi"

b = [1, 2, 3]

str(b[2]) + "hi"

b = [1, 2, 3]

b[2] = 4

b

b = [1, 2, 3]

del b[1]

b

a = []

a
type(a)

b = [1, 2, 3]

b.append(4)

b

b = [1, 2, 3]

b.append([6,7])

b

b = [1, 2, 3]

b.append(5, [6,7])

b

l = [1, 4, 3, 2]

l.sort()

l

m = ['a', 'c', 'b']

m.sort()

m

n = [1, 3, 'a', 'b', 'e', 7, 's']

n.sort()

n

o = ['a', 'c', 'b']

o.reverse()

o

b = [1,2,3]

b.index(3)

p = [1, 2, 3, 'ab', [4,5]]

p.index(4)

p[4].index(4)

b = [1, 2, 3]

b.insert(0, 4)

b
len(b)

b = [1, 2, 3]

b.insert(3, 6, 4)

b

i = [1,2,3,4,1,2,3,4]

i.remove(2)
i.remove(2)

i

b = [1,2,3]

q = b.pop()

b, q

i = [1,2,3,4,1,2,3,4]

i.count(2)

b = [1,2,3]

b.extend([4,5])

b

b = [1,2,3]

b.extend([[4,5]])

b

b = [1,2,3]

b += [4,5]

b

b = [1,2,3]
r = [4,5,6]

b.extend(r)

b



melon_rank = ['after like', 'attention', 'pink venom']

melon_rank.append('forever 1')

melon_rank

melon_rank = ['after like', 'attention', 'pink venom']

melon_rank.insert(3, 'forever 1')

melon_rank

melon_rank = ['after like', 'attention', 'pink venom']

melon_rank.extend(['forever 1'])

melon_rank

melon_rank = ['after like', 'attention', 'pink venom', 'forever 1']

melon_rank.insert(3, 'hype boy')

melon_rank

melon_rank = ['after like', 'attention', 'pink venom', 'hype boy', 'forever 1']

melon_rank.pop()

melon_rank

melon_rank = ['after like', 'attention', 'pink venom', 'hype boy', 'forever 1']

del melon_rank[4]

melon_rank

melon_rank = ['after like', 'attention', 'pink venom', 'hype boy', 'forever 1']

melon_rank.remove('forever 1')

melon_rank

