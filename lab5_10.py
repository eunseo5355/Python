# import compare
# from compare import min_max
from compare import *

# 프로그램 시작
l = [3, 5, -2, 20, 9]  # 리스트 초기화

m1, m2 = min_max(l)  # 함수 호출하여, 두 개의 반환값 받기
# m1, m2 = compare.min_max(l)

# 출력
print("최소값:", m1)
print("최대값:", m2)
