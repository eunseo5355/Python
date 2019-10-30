"""
100까지의 짝수를 출력하라.

출력예)
2 4 6 8 ....100
"""

for x in range(2, 101, 2):
    print(x, end=" ")
print()
for x in range(100, 0, -2):
    print(x, end=" ")
print()
for x in "abc":
    print(x, end=" ")
print()

# while 문 사용
i = 2
while (i < 101):
    print(i, end=" ")
    i += 2