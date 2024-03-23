# Chapter 2-1
# print 사용법

#기본 출력
print('Python Start')
print("Python Start")
print('''Python Start''')
print("""Python Start""")

#자동 줄바꿈됨
print()

# separator 옵션
print('P','Y','T','H','O','N',sep='')
print('010','1234','5678',sep='-')
print('python','google.com',sep='@')
print()

#end 옵션 : 줄바꿈이 일어나지 않음
print("Welcome to", end=" ")
print('IT News',end='!')
print('Web Site')
print()

#file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

#format 사용(d : 정수, s : 문자열, f : 소수)
print('%s %s' % ('one','two'))
print('{} {}'.format('one',2))
print('{1} {0}'.format('one','two'))#순서를 지정하여 출력
print()

# %s
print('%10s' % ('nice'))#10개의 자리수(왼쪽으로 공백)
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))#10개의 자리수(오른쪽으로 공백)
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))#공백을 _로 채워서 출력
print('{:^10}'.format('nice')) #텍스트를 중앙정렬해서 출력

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))#5글자만 출력 후 나머지는 절삭
print('{:10.5}'.format('pythonsyudy'))#공간은 10개를 확보하나 5글자만 출력
print()

# %d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f
print('%1.2f' %(3.142345675)) #정수부.소수부
print('{:f}'.format(3.141592))

print("%06.2f" % (3.151592653589793))#공백을 0으로 채움
print('{:06.2f}'.format(3.14159256523))
print()

# 파이썬 3가지 print formatting
### 3가지 Format Practices

x=50
y=100
text=30718123
n='Lee'

# 출력1
ex1 = 'n=%s, s=%s, sum=%d' %(n, text, (x+y))
print(ex1)

# 출력2
ex2 = 'n={n}, s={s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3 =>fstring
ex3 = f'n={n}, s={text}, sum={x+y}'
print(ex3)
print()


#구분기호
m=100000000
print(f'{m:,}') #천단위 구분기호 표시
print()

#정렬
# ^ : 가운데 정렬, < : 왼쪽 정렬, > : 오른쪽 정렬
t=20
print(f't : {t:10}') #10자리 확보
print(f't center : {t:^10}') #가운데 정렬
print(f't right :{t:>10}') #오른쪽 정렬
print(f't left : {t:<10}') #왼쪽 정렬
print()

print(f't center : {t:*^10}') #빈칸을 *으로 채워서 가운데 정렬
print(f't center : {t:#^10}') #빈칸을 #으로 채워서 가운데 정렬
