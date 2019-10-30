"""
두 점의 x좌표, y좌표 를 매개변수로 받아서, 기울기를 반환하는 slope()함수,
y 절편을 반환하는 y_intercept 함수
x 절편을 반환하는 x_intercept 함수
를 포함하는 line.py 파일을 정의한다.
"""


def slope(x1, y1, x2, y2):
    slope = float(y2 - y1) / float(x2 - x1)
    return slope


def y_intercept(x1, y1, x2, y2):
    y_intercept = y1 - slope(x1, y1, x2, y2) * x1
    return y_intercept


def x_intercept(x1, y1, x2, y2):
    x_intercept = y_intercept(x1, y1, x2, y2) / (-1*slope(x1, y1, x2, y2))
    return x_intercept
