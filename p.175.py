import random  # random 정수를 발생시키기 위해 포함

num = random.randint(1, 100)  # 1과 100 사이의 난수를 발생시킴

print("1부터 100 사이의 숫자를 맞추시오.")

i = 0

while i < 10:
    x = int(input("숫자를 입력하시오:"))
    i = i + 1
    if x < num:
        print("낮음!")
    elif x > num:
        print("높음!")
    else:
        break

if x == num:
    print("축하합니다. 시도횟수=", i)
else:
    print("정답은 ", num)
