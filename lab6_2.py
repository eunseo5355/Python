"""
사용자로부터 점수를 입력받아, 이를 리스트에 저장하고, 평균을 출력하라.
입력된 점수는 list 형식으로 출력한다.
점수의 끝은 음수로 확인한다.
"""

Score = []  # 리스트 초기화
sum =0  # 합 구하기
count =0  # 점수 개수를 세기 위한 변수
while True:  # 음수가 들어올 때까지 반복
    num = int(input("점수: "))  # 점수 입력 받기
    if num < 0:  # 음수이면 반복문 탈출
        break
    sum += num  # 점수 합하기
    count += 1  # 갯수 증가
    Score.append(num)  # 리스트 추가

print("입력된 점수:", Score)  # 리스트 출력

if count != 0:
    print("평균: %.2f" % (sum/count))  # 평균 출력
else:
    print("입력된 점수가 없습니다.")
print(Score[::2])
print(Score.index(80))