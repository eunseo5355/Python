"""
팩토리얼 계산 과정과 값을 출력하라.

입력 예)
양의 정수: 5
출력 예)
5! = 5*4*3*2*1 = 120
"""
num = int(input("양의 정수:"))

i = 1
f = 1
g = num

while i <= num:
    f *= i
    i += 1
    if g == num:
        print("%d! = %d *" % (num, g), end=" ")
    elif g < num and g > 1:
        print("%d *" % g, end=" ")
    elif g == 1:
        print("%d = %d" % (g, f), end=" ")
    g = g - 1
