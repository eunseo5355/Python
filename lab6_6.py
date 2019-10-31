"""
한 변의 길이가 50이하인 직각 삼각형의 세변의 길이를 출력하라.
출력 예)
[3, 4, 5]
[5, 12, 13]
[6, 8, 10]
...
"""
a = []  # 리스트 초기화
for x in range(1, 51):  # x값은 1에서 50까지 변화
    for y in range(x, 51):  # y값은 x에서 50까지 변화
        for z in range(y, 51):  # z값은 y에서 50까지 변화
            if z ** 2 == x ** 2 + y ** 2:  # 직각삼각형의 조건에 맞으면
                a.append([x, y, z])  # 리스트에 추가
# 리스트를 출력
for i in range(len(a)):
    print(a[i])

"""
# 리스트 압축 이용하기
a = [[x, y, z] for x in range(1, 51) for y in range(x, 51) for z in range(y, 51) if z**2 == x**2+y**2]

for i in range(len(a)):
    print(a[i])
"""