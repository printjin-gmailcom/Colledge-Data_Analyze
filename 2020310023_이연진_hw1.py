"""### No. 1
### 최근 공개된 iPhone 14 Pro의 출고가는 256GB 기준 1,700,000원으로 발표되었습니다.
### 이를 24개월 무이자 할부로 결제할 때, 한 달에 내야하는 금액을 계산하세요.
### 단, 소수점은 제외하고 원 단위로만 표기해주세요.
"""

iphone = 1700000
month = 24

print(iphone // month)



"""## No. 2
### 다음 문자열을 이용하여, "개구쟁이 뽀로로"를 출력하세요.
### a = "언제나 즐거운 개구쟁이 꼬마펭귄 뽀로로"
"""

a = "언제나 즐거운 개구쟁이 꼬마펭귄 뽀로로"

a[8:12] + a[-4:]



"""## No. 3
### 제 방에는 의자 6개와 테이블 2개가 있습니다.
### f 문자열 포매팅과 변수를 활용하여, 다음과 같이 출력하세요.
### '내 방에는 의자 6개가 있다'
### '내 방에는 테이블 2개가 있다'
"""

chair = '의자 6'
table = '테이블 2'

print(f'내 방에는 {chair}개가 있다. \n내 방에는 {table}개가 있다.')



"""## No. 4
### 함수를 활용하여, a=['e', 'b', 'd', 'a', 'c']를 ['e', 'd', 'c', 'b', 'a']로 바꿔 출력하세요.
"""

a=['e', 'b', 'd', 'a', 'c']

a.sort(reverse=True)

a



"""## No. 5
### (1) 빈 리스트를 만든 후,
### (2) 해당 리스트에 1,2,3,4를 추가하여 [1,2,3,4]를 출력하세요.
### (3) 이후 다시 1,2,3을 제거하여 [4]를 출력하세요.
"""

list = []

list

list.append(1)
list.append(2)
list.append(3)
list.append(4)

list

del list[:3]

list

