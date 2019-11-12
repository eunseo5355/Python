"""
입력하는 문장의 단어의 개수를 출력하시오. 대소문자 구별을 하지 않게 처리하라.
“'.,!?()/ 는 단어가 아니다.

입력예)
문장: While The Python Language Reference describes the exact syntax and semantics of the Python language,
this library reference manual describes the standard library that is distributed with Python.
It also describes some of the optional components that are commonly included in Python distributions.

출력예)
단어의 개수:
"""


def out(w):
    """
    인용부호를 제거하여 단어를 반환
    :param w: 단어
    :return: 인용부호 제거한 단어
    """
    o = ""
    for ch in w:
        if ch.isalpha():  # 만약 ch가 알파벳이라면
            o += ch  # o에 추가
    return o.lower()


s1 = input("문장:").split()  # 문장 입력 받기
s2 = set()

for i in s1:
    s2.add(out(i))  # 함수를 호출하여 나온 반환값을 s2에 추가

print("단어의 개수:", len(s2))  # 단어 개수 출력
