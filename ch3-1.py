# 파이썬 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀸스)
list : 리스트(시퀸스)
tuple : 튜플(시퀸스)
set : 집합
dict : 사전
"""

#데이터 타입
str1 = "Python"
bool1 = True
str2 = 'Anaconda'
float_v = 10.0
int_v = 7
list = [str1, str2]
print(list)
dict = {
    'name':'Machine Learning'
    ,'version':2.0
}
tuple = (7,8,9) # tuple = 7,8,9 도 가능
set = {7,8,9}


# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x의 y제곱 == x ** y
"""

#정수 선언
i = 77
i2 = -14
big_int = 777777777777777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.99999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

#실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

#연산 실습
i1 = 39
i2 = 939
big_int1 = 77777777777777777777777777777
big_int2 = 3215468212222222222222222222
f1 = 1.234
f2 = 3.939

# 연산
print(">>>>>>>>>>>>>>>")
print("i1+i2 = ",i1+i2)
print("f1/f2 = ",f1+f2)
print("big_int1*big_int2 = ",big_int1*big_int2)
print()

# 형 변환 실습
a=3.
b=6
c=.7
d=12.7

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) #True : 1, Flase : 0
print(float(False))
print(complex(3))
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))
x,y=divmod(100,8)
print(x,y)
print(pow(5,3))
print(5**3)
print()

# 외부 모듈
import math

print(math.pi)
print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정수
print(math.floor(4.8)) #x이하의 수 중에서 가장 큰 정수
print()



