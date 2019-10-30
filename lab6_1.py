"""
사용자로부터 문자열을 입력받아서, 중간의 문자(들)을 출력하라.
king 인 "in", bravo 인 경우'a'가 출력되어야 한다. slicing 을 이용하라.
작성일: 2019. 10. 24.
"""


word = input("문자열:")
a = len(word)//2

if len(word) % 2 == 0:  # 짝수인 경우
    print(word[a-1:a+1])
else:  # 홀수인 경우
    print(word[a])