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