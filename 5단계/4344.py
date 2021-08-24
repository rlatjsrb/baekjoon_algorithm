case = int(input())
for i in range(case):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    count = 0
    for i in a[1:]:
        if i > avg:
            count += 1
    print('{:.3f}%'.format(count/a[0]*100))
