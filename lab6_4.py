"""
사용자로부터 한 줄에 여러 개의 숫자를 입력받는다.
입력 받은 숫자들을 역순으로 출력하라.
입력 받은 숫자의 합도 출력하라.
입력 예)
숫자를 입력: 5 7 9 10 4 -5 7
출력 예)
역순: 10 9 7 7 5 4 -5
합:
"""
l = input("숫자를 입력:").split()

# 숫자로 변환하여 역순으로 정렬(참고)
intl = sorted(l, key=int, reverse=True)
print(intl)

# 문자열 형태로 역순으로 정렬(참고)
intl = sorted(l, reverse=True)
print(intl)

# 문제 풀이: 각 요소를 int 로 바꾼 후 정렬
intl = []  # 빈 리스트로 초기화, 정수로 변환 후 저장할 예정
sum = 0  # 합을 저장할 변수
# 리스트의 각 요소를 정수로 변환하여 intl 에 추가
for i in range(len(l)):
    intl.append(int(l[i]))  # 정수로 변환하여 intl 에 추가
    sum += intl[i]  # 합 구하기

# 출력
print("역순:", sorted(intl, reverse=True))
print("합:", sum)

