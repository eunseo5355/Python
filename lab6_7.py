"""
C:\temp\data.txt 파일에 한 줄에 하나씩 과일 이름을 5개 넣는다.
사용자로부터 과일 이름을 입력받아서, 해당 과일이 data.txt 파일에 있는 과일이면,
"재고가 있습니다." 없는 과일이면, "재고가 없습나다." 를 출력한다.
입력 예)
과일명: 사과
출력 예)
사과는 재고가 있습니다.
"""

# 데이터를 저장할 리스트 초기화
data = []
"""
파일의 path는 \\ 두개로 구별
한글 파일을 읽기 위해서는 encoding을 UTF8으로 설정
"""
# 파일 열기
f = open("C:\\Temp\\data.txt", "r", encoding='UTF8')
# 입력 받기
name = input("과일명:")

"""
# 발견했는지 여부 저장
found = False
"""

# 파일에서 데이터를 읽어서 data 리스트에 저장
for line in f.readlines():  # 한 줄씩 읽어서 line 변수에 저장
    data.append(line.strip())

"""
    if line.strip() == name:  # 마지막에 있는 줄바꿈은 빼고 name 과 비교
        # 발견헸으면
        print("%s는(은) 재고가 있습니다." % name)
        found = True
        break  # 반복 벗어나기
# 반복문 끝까지 발견하지 못했다면
if found == False:
    print("%s는(은) 재고가 없습니다." % name)
"""

if name in data:
    print("%s는(은) 재고가 있습니다." % name)
else:
    print("%s는(은) 재고가 없습니다." % name)