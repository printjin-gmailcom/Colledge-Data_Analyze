a = True
b = False

a and b

a or b

not a



c = False
d = False

c and d

c or d

not c



money = 2000
card = True

if money >= 3000 or card:
    print("택시")
else:
    print("도보")

money = 2000
card = True

if money >= 3000 and card:
    print("택시")
else:
    print("도보")





x = 5
print(1<x<5)

print((2==2)) and (5!=3)

if 3>4:
    print('Hello')

if True:
    if False:
        print('1')
        print('2')
    else:
        print('3')
        print('4')
else:
    print('5')
print('6')





1 in [1, 2, 3]

1 not in [1, 2, 3]

'a' in ('a', 'b', 'c')

'j' not in 'python'



pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어가라")



pocket = ['paper', 'cellphone', 'key', 'card']
card = True
if 'money' in pocket:
     print("택시")
else:
    if 'card' in pocket:
         print("택시2")
    else:
         print("도보")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시")
elif card:
     print("택시2")
else:
     print("도보")



pocket = ['paper', 'cellphone', 'card']
if 'money' in pocket: print("택시")
elif 'card' in pocket : print("택시2")
else: print("도보")



time = '14:15'

if ':00' in time:
    print("정각입니다")
else:
    print("정각이 아닙니다")

time = '16:00'
if time[-2:] == '00':
    print('정각입니다')
else:
    print('정각이 아닙니다')



phone = '02-111-2222'

if phone[:2] =='02':
    print('서울')
elif phone[:3] == '031':
    print('경기도')
elif phone[:3] == '032':
    print('인천')
else:
    print('그외')

tel = '02-111-2222'

tel2 = tel.split('-')

if tel2[0] == '02':
    print('서울')
elif tel2[0] == '031':
    print('경기도')
elif tel2[0] == '032':
    print('인천')
else:
    print('그외')



a = 3
b = 4
c = 6

max(a,b,c)

a = 3
b = 4
c = 6

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)













treeHit = 0

while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")



coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break





