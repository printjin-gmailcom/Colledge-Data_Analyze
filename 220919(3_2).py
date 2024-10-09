a = set([1,2,3])
a

b = {1,2,3,4}
set(b)



c = set("Hello")
c



t1 = tuple(a)
t1

t1 = tuple(a)
t1[0]



a = set([1,2,3])
l1 = list(a)
l1

a = set([1,2,3])
l1 = list(a)
l1[0]



s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2

s1.intersection(s2)

s1 | s2

s1.union(s2)

s1 - s2

s1.difference(s2)



a = set([1, 2, 3])
a.add(4)
a

a = set([1, 2, 3])
a.update([4, 5, 6])
a

a = set([1, 2, 3])
a.remove(2)
a



a1 = [1,1,1,1,2,2,2,'p','p','a','p',2,2,1,1]

a2 = set(a1)

a3 = list(a2)

a3



c = True
d = False

type(c), type(d)



1 == 1

2 > 1

2 < 1



#자료값이 비어있거나 0인 경우는 False

bool('python')

bool('')

bool([1,2,3])

bool([])

bool(0)

bool(3)



print(bool({1:1}))
print(bool({}))
print(bool(True))
print(bool(False))



print(bool(False==False))
print(bool([]==False))
print(bool('abc'==True))
print(bool(bool('abc')==True))





e = [1, 2, 3]
id(e)

e = [1, 2, 3]
f = e
id(f)

e is f



e = [1, 2, 3]
id(e)

e = [1, 2, 3]
f = e[:]
id(f)

e is f



e = [1, 2, 3]
e = f
e[1] = 4
f

e = [1, 2, 3]
f = e[:]
e[1]=4
f



g, h = ('python', 'life')
print(g)
print(h)

g,h = h,g
print(g)
print(h)



i=[1,2,3]
j=[1,2,3]
i is j

i=[1,2,3]
j=[1,2,3]

print(id(i))
print(id(j))



