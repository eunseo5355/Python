"""
문제: 사용자로부터 두 개의 문자열을 한 줄에 입력받아 두 줄로 출력하시오.
입력 예)
입력: 사과 두개
출력 예)
사과
두개
"""

a, b = input("입력:").split(" ")
print(type(a))
print(a)
print(b)


s = input("입력:")
l = s.split()
print(type(l))
print(l[0])
print(l[1])

l = input("입력:").split()
print(type(l))
print(l[0])
print(l[1])

l = input("입력:").split()
for i in l:
    print(i)