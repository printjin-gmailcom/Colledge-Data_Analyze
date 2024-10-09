# 입력값
# print(a)

a = input()
print(a)

a = input()
print(a*2)



a = input('입력: ')
print('출력:', a)
print(type(a))

a = input('입력: ')
b = input('입력: ')
print(a + b)

a = int(input('입력: '))
b = int(input('입력: '))
print(a + b)



a = 123
print(a)

a = "Python"
print(a)

a = [1, 2, 3]
print(a)



print("life" "is" "too short")

print("life"+"is"+"too short")

print("life", "is", "too short") #띄어쓰기는 , 사용



print('**', '***')
print('**' + '***')
print('**' '***')
print('**''***')



f = open("new1.txt", 'w')
f.close()

# r 	읽기모드 - 파일을 읽기만 할 때 사용
# w 	쓰기모드 - 파일에 내용을 쓸 때 사용
# a 	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용



f = open("new2.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("new2.txt", 'r')
line = f.readline()
print(line)
f.close

f = open("new2.txt", 'r')
while 1:                    #True에 해당하는 값만 써도 돌아감. 교재에 없음. 참고정도만.
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("new2.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("new2.txt", 'r')
lines = f.readlines()
print(lines)

f = open("new2.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("new2.txt", 'r')
data = f.read()
print(data)
f.close()



f = open("new2.txt",'a')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()



f = open("new3.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("new3.txt", "w") as f:
    f.write("Life is too short, you need python")



삼성전자 55,900
lg에너지솔류션 499,000
sk하이닉스 90,500

f = open("stock1.txt", 'w')
f.write("삼성전자 55,900 \nlg에너지솔루션 499,000 \nsk하이닉스 90,500 \n")
f.close()



f = open("stock2.txt", 'w')
f.write("삼성전자 55,900 \n")
f.write("lg에너지솔루션 499,000 \n")
f.write("sk하이닉스 90,500 \n")
f.close()



f = open("stock1.txt",'a')
f.write("삼성바이오로직스 847,000 \n")
f.write("삼성sdi 627,000 \n")
f.close()

