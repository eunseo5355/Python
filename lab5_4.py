"""
매개변수로 넘어온 리스트에서 최대값을 반환하는 get_max 함수를 정의한다.
프로그램에서,
l1 = [3, 5, -2, 20, 9], l2 = [-4, 374, 3, 1, 4, 7, -23]을 정의한 후, 각각의 최대값을 출력하고,
두  최대값의 합을 출력하라.
출력 예)
l1의 최대값: 20
l2의 최대값: 374
l1과 l2의 최대값의 합 = 394
"""


def get_max(l):  # get_max 함수 정의
    m = l[0]  # 리스트 첫번째 요소로 초기화
    for i in range(0, len(l)):  # 리스트 마지막 요소까지 반복
        if m <= l[i]:
            m = l[i]
    return m  # m 반환


l1 = [3, 5, -2, 20, 9]  # l1 정의
l2 = [-4, 374, 3, 1, 4, 7, -23]  # l2 정의

a = get_max(l1)
b = get_max(l2)

print("l1의 최대값:", a)  # l1의 최대값 출력
print("l2의 최대값:", b)  # l2의 최대값 출력
print("l1과 l2의 최대값의 합 =", a + b)  # l1과 l2의 최대값의 합 출력