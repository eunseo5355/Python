# x좌표와 y좌표를 입력 받아, 원점에서부터의 거리를 출력하라.
from math import*

a = int(input("x좌표:"))
b = int(input("y좌표:"))

print("원점으로부터의 거리:", sqrt(a*a+b*b))