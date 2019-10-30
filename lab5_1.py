"""
사용자로부터 정수를 입력받아서, 1부터 해당 정수까지 출력한다.
print_int 함수를 먼저 정의한다. print_int 함수는 정수를 매개변수로 받아서,
1부터 해당 매개변수 값까지 출력하는 함수이다.
사용자로부터 정수를 입력받아, print_int 를 호출한다.
"""


def print_int(num):
    """
    1부터 num 까지 정수 출력
    :param num: 마지막 수
    :return: 없음
    """
    for i in range(1, num + 1):
        print("%d" % i, end=" ")


a = int(input("정수 입력:"))  # 입력 받기
print_int(a)  # 호출
