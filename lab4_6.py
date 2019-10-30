"""
유클리드 호제법은 이용하여, 최대공약수와 최소공배수를 구하라.
최대공약수가 없는 경우 "최대공약수: 없습니다."가 출력된다.

입력 예)
첫번째 수: 18
두번째 수: 42
출력 예)
최대공약수:
최소공배수:
"""
a = int(input("첫번째 수:"))
b = int(input("두번째 수:"))

if a > b:
    x, y = a, b
else:
    x, y = b, a

while y != 0:
    r = x % y
    x, y = y, r

print("최대공약수:", end=" ")
if x == 1:
    print("없습니다.")
else:
    print(x)

print("최소공배수:", a*b//x)




