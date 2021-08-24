case = int(input())
for i in range(case):
    score = input()
    score = list(score)
    sum = 0
    a = 1
    for i in score:
        if i == 'O':
            sum += a
            a += 1
        else:
            a = 1
    print(sum)