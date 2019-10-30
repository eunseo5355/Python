"""
삼각현의 넓이를 구하는 함수 tri_area 를 정의한다. 밑변 w와 높이 h를 매개변수로 받아서,
넓이를 반환한다.
프로그램에서, 사용자로부터 밑변과 높이를 입력 받아거, 넓이를 풀력하라.
tri_area 를 호출할 때, 키워드 인수를 사용한다.

입력 예)
밑변: 5
높이: 10
출력 예)
삼각형의 넓이: 25
"""


def tri_area(w, h):
    """
    삼각형의 넓이를 반환
    :param w: 밑변
    :param h: 높이
    :return: 넓이
    """
    t = w
    w = w*2
    print("w in tri_area:%d" % w)
    return w * h * 1 / 2


# 프로그램 시작
w = int(input("밑변:"))
h = int(input("높이:"))

print("삼각형의 넓이:%.2f" % (tri_area(w=w, h=h)))
