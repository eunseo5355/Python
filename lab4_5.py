"""
두 정수를 입력받아, 두 정수의 약수를 모두 출력하라.
만약 1이외의 다른 공약수가 없는 경우에는, "공약수가 없습니다."를 출력하라.

입력 예1)
첫번째 수: 15
두번째 수: 45
출력 예1)
공약수: 3

입력 예2)
첫번째 수: 16
두번째 수: 45
출력 예2)
공약수 없습니다.
"""
a = int(input("첫번째 수:"))
b = int(input("두번째 수:"))

# 큰 수를 a, 작은 수를 b에 배정
if a > b:
    t = a  # a 값을 t라는 곳에 임시 보관
    a = b  # b 값이 a에 저장된다. a 초기값은 없어짐
    b = t  # a의 초기값은 t에 저장되어 있으므로, 이 값을 b에 저장

# 첫번째 수의 약수 구하기
print("%d의 약수:" % a, end=" ")
for i in range(1, a + 1):
    if a % i == 0:
        print(i, end=" ")
print()

# 두번째 수의 약수 구하기
print("%d의 약수:" % b, end=" ")
for i in range(1, b + 1):
    if b % i == 0:
        print(i, end=" ")
print()

# 출력
print("공약수:", end=" ")

# 최대공약수를 g에 배정
g = 1

# 2부터 a까지 1씩 등가시키며 약수 찾기
for i in range(2, a + 1):
    if a % i == 0 and b % i == 0:
        g = i  # 최대공약수 바꾸기
        print(i, end=" ")  # 공약수 출력

# 만약 1이 아닌 공약수가 없다면 "없습니다" 출력
if g == 1:
    print("없습니다.")
else:
    print()
    print("최대공약수:", g)