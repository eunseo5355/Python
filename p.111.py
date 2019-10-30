"""
문자열의 중앙에 있는 문자를 출력한다.

입력 예1)
문자열을 입력하시오: weekday
출력 예1)
중앙글자는 k

입력 예2)
문자열을 입력하시오: string
출력 예2)
중앙글자는 r i
"""
word = input("문자열을 입력하시오:")

if len(word) % 2 != 0:
    print("중앙글자는 ", word[len(word)//2])
else:
    print("중앙글자는 %s %s" % (word[len(word)//2-1], word[len(word)//2]))

