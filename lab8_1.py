"""
주제: 클래스 정의
작성일: 2019. 11. 19.
"""


class Counter:
    """
    갯수를 세는 클래스
    """

    def reset(self):
        """
        counter 를 0으로 reseet
        :return: 없음
        """
        self.count = 0

    def inc(self, i):
        """
        Counter 를 하나 증가
        :return: 없음
        """
        self.count += i

    def current(self):
        """
        현재 값을 반환
        :return: 현재 값
        """
        return self.count


# 프로그램 시작

a = Counter()  # 생성자를 호출하여 Counter 객체 생성하여 변수 a에 배정

a.reset()  # a가 self가 되어 메쏘드 reset이 호출된다
           # reset()의 매개변수를 따로 보낼 필요 없다
           # a가 저절로 self로 전달된다
           
a.inc(1)  # a를 증가시키기 위해 inc() 메쏘드를 호출한다. self 이외에 매개변수 i가 있으므로,
          # i값을 전달한다

print("a의 현재값:", a.current())
a.inc(2)
print("a의 현재값:", a.current())