"""
클래스 직사각형(Rectangle)의 가로(w),세로(h)가 멤버 애트리뷰트이다.
init(i, j)# 가로가 i, 세로가 j로 초기화
area() # 넓이를 반환
length() # 둘레를 반환
print() # 가로와 세로를 출력 예) 가로 3, 세로 5인 직사각형입니다.

프로그램에서는,
새로운 직사각형 객체를 생성하여 가로 3, 세로 5 로 설정하고,
메쏘드를 이용하여 가로 세로 출쳑,둘레를 출력하라.
"""


class Rectangle:
    """
    직사각형 클래스 정의
    """

    def init(self, i, j):
        """
        가로 세로 초기화
        :param i: 가로
        :param j: 세로
        :return: 없음
        """
        self.w = i  # 가로
        self.h = j  # 세로

    def area(self):
        """
        면적을 반환
        :return: 면적
        """
        return self.w * self.h

    def length(self):
        """
        둘레 반환
        :return: 둘레
        """
        return self.w * 2 + self.h * 2

    def print(self):
        """
        가로 세로를 출력
        :return: 없음
        """
        print("가로 %d, 세로 %d인 직사각형입니다." % (self.w, self.h))


# 프로그램 시작

r = Rectangle()  # Rectangle 클래스의 객체를 생성하여 변수 r에 저장
r.init(3, 5)
r.print()
print("넓이: %d\n둘레: %d" % (r.area(), r.length()))
