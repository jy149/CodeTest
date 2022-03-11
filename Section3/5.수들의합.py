'''
N개의 수로된 수열 A[1] ~ A[N], i번째부터 j번째수까지의 합 A[i] + A[i+1] + ... + A[j-1] + A[j] 가 M이되는 경우의 수
-> 연속된 수의 합이 M이되는 경우
'''
import sys
sys.stdin = open("input_5.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1

tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)
