"""
Counter 틀래스에 dec 메쏘드를 추가하시오. 매개변수가 넘어오지 않으면 1을 감소시키고,
매개변수가 있다면 매개변수값만큼 감소시킨다. 단, counter 값은 최소 0이다.

프로그램에서,
dec를 매개변수 없이 호출한 후, Counter 값을 출력
dec의 매개변수를 100으로 호출한 후, Counter 값을 출력
"""


class Counter:
    """
    갯수를 세는 클래스
    """
    def __init__(self):  # 생성자 메쏘드(특별한 메쏘드)
        self.count = 0

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

    def dec(self, i=1):
        """
        counter를 감소시킨다. 만약 counter가 0보다 작으면 0으로 설정한다.
        :param i:
        :return:
        """
        self.count -= i
        if self.count < 0:
            self.reset()  # 메쏘드안에서 다른 메쏘드 호출 가능
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

a.dec()
print("a의 현재값:", a.current())
a.dec(100)
print("a의 현재값:", a.current())