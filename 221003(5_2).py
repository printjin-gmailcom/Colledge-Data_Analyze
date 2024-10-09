a = 123
a

b = -2
b, type(b)

c = 1.2
c, type(c)

d = 3.5e2
d, type(d)

354//16

354%16

e = '123'
e, type(e)

f = 'python's favorite food is perl'
f

g = "'pyhton is very easy' he says"
g

h = 'h'
h # 문자열

i = h
i # 변수

j = 'ab\'cd'
j, len(j)

k = 'Life is too short, you need python'
k [0], k[15], k[-2]

l = 'Life is too short, you need python'
l[0:4], type(l[0:4])

number1 = 'three'
'I eat %s apples' %number1

'I eat %s apples' %'three'

'I eat %10s apples' %'three'

'I eat %-10s apples' %'three'

number2 = 3.141592
'I eat %4f apples' %number2

number2 = 3.141592
'I eat %10.4f apples' %number2

number2 = 3.141592
'I eat %-10.4f apples' %number2

name1 = '홍'
age1 = 20
'내 이름은 %s, 나이는 %d' %(name1, age1)

name1 = '홍'
age1 = 20
f'내 이름은 {name1}, 나이는 {age1}'

'%10s' % 'hi'

'%-10s' % 'hi'

f'{"hi":$^10}'

f'{"hi":$<10}'



# find 없을시 -1
# index error발생

m = 'python'
m[1]

n = ['ab','cd','ef']
n[1]+n[2], len(n)

o = ['c','d',2,1]
o.sort()

p = ['c','d','2.1']
p.sort()
p

q = ['c','d','a','f','ee']
q.sort(reverse = True)
q

r = ['c','d','a','f','ee']
r.reverse()
r

s = [1,2,3]
s[2] = 3
s.index(3) = 2
s

t = [1,2,3]
t[0] = 4
t

u = [1,2,3]
u.remove(2)
u

v = [1,2,3]
v.pop(2), v

w = (1,)
type(w)

x = (1)
type(x)

y = (0) + (1,2,3)
y

z = (0,) + (1,2,3)
z

a = [1,2,3]
1 in a

b = {1:'a',2:'b',3:'c'}
1 in b, 'b' in b

c = {1:'a',2:'b',3:'c'}
c['name']

