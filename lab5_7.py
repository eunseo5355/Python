"""
매개변수로 넘어온 리스트에서 최소값과 최대값을 반환하는 함수 min_max 를 정의한다.
프로그랩에서,
l = [3, 5, -2, 20, 9]을 정의한 후, min_max 를 호출하여, 최소값은 m1, 최대값은 m2에 저장한 후
이를 출력하라.

출력 예)
최소값: -2
최대값: 20
"""


def min_max(li):
    """
    매개변수로 넘어온 리스트에서 최소값과 최대값을 반환하는 함수
    :param li: 리스트
    :return: 최소값, 최대값
    """
    # min 와 max 를 리스트 0번째 요소로 초기화
    min = li[0]
    max = li[0]
    # 반복문을 돌면서 최소, 최대값 찾기
    for i in range(len(li)):
        if min > li[i]:  # 현재 값이 min 보다 작으면
            min = li[i]  # 최소값 변경
        elif max < li[i]:  # 현재 값이 max 보다 크면
            max = li[i]  # 최대값 변경
    return min, max  # 최소, 최대값을 반환


# 프로그램 시작
l = [3, 5, -2, 20, 9]  # 리스트 초기화

m1, m2 = min_max(l)  # 함수 호출하여, 두 개의 반환값 받기

# 출력
print("최소값:", m1)
print("최대값:", m2)