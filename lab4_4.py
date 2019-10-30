"""
정수의 각 자리수의 합을 출력하라.

입력예)
정수: 546
출력예)
자리수의 합: 15
"""
num = int(input("정수:"))
i = 0
while(num>0):
    a = num % 10
    i += a
    num = num//10
print("자리수의 합:", i)
