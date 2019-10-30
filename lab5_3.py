"""
두 수를 매개변수로 받아, 두 수 중 작은 수를 반환하는 min 함수를 정의한다.
프로그램에게는 사용자로부터 두 수를 입력받아 min 함수를 호출한 후 작은 값을 출력했다.
입력예)
두 수 : 3 -5
작은 수: -5
"""


def min(a, b):
    if a > b:
        return b
    else:
        return a


i, j = input("두 수:").split()

x = int(i)
y = int(j)

z = min(x, y)

print("작은 수:", z)
