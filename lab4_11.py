"""
사용자가 입력받은 숫자만큼의 줄과 갯수의 *를 출력한다.

입력 예)
정수 입력: 5
출력 예)
*
**
***
****
*****
"""
num = int(input("정수 입력:"))
for y in range(1, num+1):
    for x in range(1, y+1):
        print("*", end="")
    print()