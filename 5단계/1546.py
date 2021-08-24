sub = int(input())
s = []
s = list(map(int, input().split()))

max_score = max(s)
sum = 0
for i in s:
    sum += i/max_score*100
print(sum/sub)