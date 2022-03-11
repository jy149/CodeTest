# 격자판 행의합, 열의합, 대각선 합의 최댓값 찾기

import sys
sys.stdin = open("input_6.txt" ,"rt")

# 격자판 N X N
n = int(input())

# 2차원 리스트
a = [list(map(int, input().split())) for _ in range(n)]
for x in a:
    print(x)

largest = - float("inf")

# 행/열의 최대합 찾기
for i in range(n):
    # 행의 합 : sum1, 열의 합 : sum2
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선 합 최대찾기
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)