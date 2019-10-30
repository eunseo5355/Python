# 두 수를 입력받아, 절대값이 큰 수, 작은 수를 출력하라.

a = int(input("첫번째 수:"))
b = int(input("두번째 수:"))

print("절대값이 큰 수의 절대값:", max(abs(a), abs(b)))
print("절대값이 작은 수의 절대값:", min(abs(a), abs(b)))