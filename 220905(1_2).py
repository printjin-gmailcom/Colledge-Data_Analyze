a = 123

a

type(a)

print(a)
print(type(a))

print(a, type(a))

b = 12.34

b

type(b)

c = 4.23e3

c

type(c)

d = 0o177

d

type(d)

e = 0o156
e

type(e)

f = 0x8ff
 g = 0xABC

f, g

print( type(f), type(g))



h = 7
i = 4

print(h + i)
print(h * i)
print(h ** i)
print(h / i)
print(h // i) #몫
print(h % i) #나머지

j = 7.2
k = 4.5

print(j + k)
print(j * k)
print(j ** k)
print(j / k)
print(j // k) #몫
print(j % k) #나머지

l = 354
m = 16

print(l // m) #몫
print(l % m) #나머지



n = "123"

print(n)

type(n)



o = "Hello World"
p = 'Python is fun'
q = """Life is too short, You need python"""
r = '''Life is too short, You need python'''

print(o,'/', p, '/', q, '/', r)

food1 = "Python's favorite food is perl"
print(food1)

say1 = '"Python is very easy." he says.'
print(say1)

food2 = 'Python\'s favorite food is perl'
say2 = "\"Python is very easy.\" he says."

print(food2,'/', say2)



# \ = 백슬래시 (두 국가 예외 : 한국에서는 원화, 일본에서는 엔화로 표기)
# \n 	 문자열 안에서 줄을 바꿀 때 사용
# \t 	 문자열 사이에 탭 간격을 줄 때 사용
# \\ 	 문자 \를 그대로 표현할 때 사용
# \' 	 작은따옴표(')를 그대로 표현할 때 사용
# \" 	 큰따옴표(")를 그대로 표현할 때 사용
# \r 	 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f 	 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a 	 벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
# \b 	 백 스페이스
# \000  	 널 문자



life1 = "Life is too short\nYou need python"
print(life1)

life2 ='''
Life is too short
You need python
'''
print(life2)

life3 ="""Life is too short
You need python"""
print(life3)



head = "Python"
tail = " is fun!"
print( head + tail)

s = "python"
print(s * 2)

a = 123
n = "123"
print( a * 3, '/', n * 3 )

t = "Life is too short"
len(t)

u = '프로그래밍과 데이터 분석 - "권오성"'
print(len(u))



v = "Life is too short, You need Python"
v[0], v[3], v[7], v[-1]

w = '동해물과 백두산이'
w[0] + w[5] + w[-1]

