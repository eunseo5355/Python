"""
import 하지 말고, deepcopy 함수를 정의하라.
261페이지에 있는 프로그램을 import 하지 않고 작동해 보라.
"""
"""
scores = [10, 20, 30, 40, 50]
values = list(scores)
values[2] = 99
print(scores)
print(values)
"""

def deepcopy(l):
    """
    deepcopy 구현
    :param l: 리스트
    :return: deepcopy된 list
    """
    rl = []
    for i in l:
        rl.append(i)
    return rl


scores = [10, 20, 30, 40, 50]
values = deepcopy(scores)
print(values)
