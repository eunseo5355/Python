"""
사용자로부터 자연수를 입력받아서, factorial 값을 출력하라.

입력예)
자연수: 3
출력예)
3!=6
"""

num = int(input("자연수:"))  # 입력받기
i = 1
for x in range(1, num+1):
    i *= x
print("%d! = %d" % (num, i))