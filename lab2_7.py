# 이율, 기간, 원금을 입력받아서, 원리금 합계를 출력하라.

a = float(input("연이율:"))
b = int(input("기간(년):"))
c = int(input("원금(원):"))

print("원리금:", c*(1+a)**b)