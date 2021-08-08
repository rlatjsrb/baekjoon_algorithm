import sys
X, N = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
for i in range(X):
    if A[i] < N:
        print(A[i], end = " ")