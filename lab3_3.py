"""
문제:
사용자로부터 실수를 입력받아 절대값을 출력하라.
(단, abs 함수를 사용하지 않는다.)
"""
a = float(input("실수:"))

if a > 0:
    print("절대값:%s" % a)
if a < 0:
    print("절대값:%s" % (a*-1))
else:
    print("절대값:", 0)