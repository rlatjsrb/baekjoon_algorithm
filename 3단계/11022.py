import sys
T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    A, B = int(A), int(B)
    print('Case #{0}: {1} + {2} = {3}'.format(i+1, A, B, A + B))