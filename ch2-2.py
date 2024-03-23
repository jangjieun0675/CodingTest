# 파이썬 변수

# 기본 선언
n=700

print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x,y,z)
print()

#선언
var = 75
#재선언
var = 'change value'

print(var)
print(type(var))
print()

#object Reference
#변수 값이 할당 상태

#1. 타입에 맞는 오브젝트 생성
#2. 값 생성
#3. 콘솔 출력

print(300)
print(int(300))

n=777
m=n
print(m, type(m))
print()

m = 400
print(m, type(m))
print(n, type(n))
print()

# id(identity) 확인 : 객체의 고유값 확인
m=800
n=655

print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# 같은 오브젝트 참조
m=800
n=800
print(id(m))
print(id(n))
print(id(m)==id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfGraduate -> Method
# Pascal Case : NumberOfGraduate -> Class
# Snake Case : number_of_graduate -> 변수 선언


