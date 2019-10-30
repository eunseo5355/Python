"""
사용자가 선택하는 도형의 면적을 계산하는 프로그램을 작성해보자.
"""
num = int(input("도형을 입력하시오(1: 사각형, 2: 삼각형, 3: 원): "))
if num == 1:
    w = int(input("가로: "))
    h = int(input("세로: "))
    print("면젹= ", w*h)
elif num == 2:
    w = int(input("밑변: "))
    h = int(input("높이: "))
    print("면젹= ", w * h / 2)
else:
    r = int(input("반지름: "))
    print("면적= ", r*r*3.141592)