"""
for 문 이용하여 팩토리얼 계산하기
"""

num = int(input())
sum = 1

for i in range(1, num+1):
    sum *= i
print(sum)

print("----------------")

j = 1
sum2 = 1
a = num
while j <= num:
    sum2 *= a
    j += 1
    a -= 1
print(sum2)