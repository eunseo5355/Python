"""
학번과 점수를 dictionary 를 이용하여 5개 정도 정의한다.
사용자로부터 학번과 점수를 입력받아, 만약 기존에 해당 학번이 없으면 dictionary 에 추가한다.
성적이 높은 순으로 출력하라.
예)
학번: 20182454
점수: 49
출력 예)
"""
# dictionary 초기화
scores = {'201914090': 100, '201914091': 90, '201914092': 80, '201914093': 70, '201914094': 60}

# 입력 받기
num = input("학번:")
score = int(input("점수:"))

# 기존에 있는 키 값이 아니면 추가
if num not in scores:
    scores[num] = score

# 점수의 역순으로 학번을 정렬
l = sorted(scores, key=scores.__getitem__, reverse=True)

for i in l:  # 반복문을 이용하여 출력
    print(i)

