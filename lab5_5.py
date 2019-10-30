"""
sum_list 는 두 개의 매개변수를 받는다. 첫번째 매개변수 리스트이고, 두번째 매개변수는 start 로서
어디부터 합할 지를 의미한다. start 의 두번째 매개변수는 default 값을 0으로 가진다.
예를 들어 sun_list(l,2)는 2번째 요소부터 시작하여 리스트의 합을 구하여 반환한다.
sum_list(l)은 0번째 요소부터 시작하여 리스트의 합을 구하여 반환한다.

프로그램에서
l = [-5,4,6,10,3]을 정의하여,
sum_list(l,2)의 반환값과
sum_list(l)의 반환값을 출력하라.
출력 예)
sum_list(l,2) = 19
sum_list(l) = 18
"""


def sum_list(l, start=0):
    """
    l의 start 부터 끝까지 합을 구하여 반환
    :param l: 리스트
    :param start: 시작 인덱스. default 값은 0
    :return: 합
    """
    sum = 0
    for i in range(start, len(l)):
        sum += l[i]
    return sum


# 프로그램 시작
l = [-5, 4, 6, 10, 3]

print("sum_list(l, 2) = %d" % sum_list(l=l, start=2))
print("sum_list(l, 2) = %d" % sum_list(l, 2))
print("sum_list(l) = %d" % sum_list(l))
