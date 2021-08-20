N = int(input())
A = 0
cnt = 1
if N < 10:
    A = N * 10 + N
else:
    A = (N%10)*10 + ((N // 10) + (N % 10)) % 10
while N != A:
    A = (A % 10)*10 + ((A // 10) + (A % 10)) % 10
    cnt += 1
print(cnt)