"""
2단부터 9단까지 구구단을 출력하라.
출력 예)
2*1 = 2
2*2 = 4
...
3단
3*1 = 3
...
9단
...
9*9 = 81
"""
for i in range(2, 10):
    print("%d단\n" % i)
    for j in range(1, 10):
        print("%d * %d = %d\n" % (i, j, i*j))