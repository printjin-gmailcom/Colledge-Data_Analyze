def coins():
    for i in range(10):
            print('doge')

coins()

a = coins()

print(a)



def url(page):
    print("www.%s.com" %page)

url('naver')
url('google')

def url(page):
    return 'www.'+page+'.com'

url('naver')
url('google')

def url(page):
    return 'www.'+page+'.com'
def url2(page):
    print('www.'+page+'.com')

print(url('naver'))
url2('naver')



def alp(letter):
    return letter.split()


print(alp('abcd'))

def alp(letter):
    result = []
    for i in letter:
        result.append(i)
    return result

print(alp('abcd'))

def alp(letter):
    return list(letter)

print(alp('abcd'))

