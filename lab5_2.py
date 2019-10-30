"""
sqaure 함수는 제곱을 반환하는 함수이다. 이를 정의하라.
프로그램에서 1부터 5까지의 정수에 대해 sqaure 함수를 호출하여 제곱을 반환받은 후 아래와 같이 출력한다.
출력 예)
정수    제곱
1       1
2       4
3       9
4      16
5      25
"""


def sqaure(n):
    """
    제곱 계산
    :param n: 정수
    :return:  제곱을 반환
    """
    return n * n

# 프로그램 시작
print("정수\t제곱")

for j in range(1, 6):
    print("%d\t\t%d" % (j, sqaure(j)))
