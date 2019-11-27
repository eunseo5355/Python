"""
문자열 S를 입력받은 후에,
각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
입력 예)
2
3 ABC
5 /HTP
출력 예)
AAABBBCCC
/////HHHHHTTTTTPPPPP
"""
num = int(input())  # 반복 횟수 입력받기
for i in range(num):  # 한 줄씩 입력 받기
    R, S = input().split()
    for j in range(len(S)):
        print(S[j]*int(R), end="")
    print()

"""
max = int(input())  # 반복 횟수 입력 받기
for k in range(max):  # 한 줄씩 입력 받기
    l = input().split()  # 한줄 입력을 빈칸을 나누어 리스트에 저장
    count = int(l[0])  # 한 줄의 제일 앞 숫자는 출력 반복할 횟수
    for i in range(len(l[1])):  # 한 줄의 두번째에 입력된 각 문자열에 대하여
        for j in range(0, count):  # 반복횟수만큼 반복
            print(l[1][i],end="")  # 한줄에 붙여서 출력
    print()  # 한 줄 출력이 끝나면 줄 바꾸기
"""